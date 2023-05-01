from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.forms import SelectDateWidget

STUDENT_STATUS_CHOICES = (
    ("Freshman", "Freshman"), 
    ("Sophomore", "Sophomore"), 
    ("Junior", "Junior"),
    ("Senior", "Senior"),
    ("Graduate", "Graduate"),
)

SCHOOL_CHOICES = (
("Amherst", "Amherst College"),
("Babson", "Babson College"),
("Barnard", "Barnard College"),
("BC", "Boston College"),
("BU", "Boston University"),
("Bowdoin", "Bowdoin College"),
("Brandeis", "Brandeis University"),
("Brown", "Brown University"),
("Caltech", "California Institute of Technology"),
("CMU", "Carnegie Mellon University"),
("CMC", "Claremont McKenna College"),
("Columbia", "Columbia University"),
("Cornell", "Cornell University"),
("Dartmouth", "Dartmouth College"),
("Duke", "Duke University"),
("Emory", "Emory University"),
("Georgetown", "Georgetown University"),
("Georgia Tech", "Georgia Institute of Technology"),
("Harvard", "Harvard University"),
("HMC", "Harvey Mudd College"),
("JHU", "Johns Hopkins University"),
("MIT", "Massachusetts Institute of Technology"),
("Middlebury", "Middlebury College"),
("NYU", "New York University"),
("Tandon", "New York University Tandon School of Engineering"),
("Northwestern", "Northwestern University"),
("Pomona", "Pomona College"),
("Princeton", "Princeton University"),
("Rice", "Rice University"),
("Stanford", "Stanford University"),
("Swarthmore", "Swarthmore College"),
("Tufts", "Tufts University"),
("UC Berkeley", "University of California, Berkeley"),
("UCLA", "University of California, Los Angeles"),
("UCSD", "University of California, San Diego"),
("UCSB", "University of California, Santa Barbara"),
("UChicago", "University of Chicago"),
("Michigan", "University of Michigan, Ann Arbor"),
("UNC", "University of North Carolina at Chapel Hill"),
("Notre Dame", "University of Notre Dame"),
("UPenn", "University of Pennsylvania"),
("USC", "University of Southern California"),
("UT Austin", "University of Texas at Austin"),
("UVA", "University of Virginia"),
("UW", "University of Washington"),
("Vanderbilt", "Vanderbilt University"),
("WashU", "Washington University in St. Louis"),
("Wellesley", "Wellesley College"),
("Williams", "Williams College"),
("Yale", "Yale University"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True)
    school_name = models.CharField(max_length=100, choices=SCHOOL_CHOICES, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(4)], null=True, blank=True)
    student_status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    calendly_link = models.URLField(blank=True)
    zoom_meeting_link = models.URLField(blank=True)

    
    def __str__(self):
        return f'{self.user.username} Profile'


SKILL_CHOICES = (
    ('C++', 'C++'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('JavaScript', 'JavaScript'),
    ('HTML/CSS', 'HTML/CSS'),
    ('Ruby', 'Ruby'),
    ('PHP', 'PHP'),
    ('Swift', 'Swift'),
    ('Kotlin', 'Kotlin'),
    ('C#', 'C#'),
    ('SQL', 'SQL'),
    ('Data Analysis', 'Data Analysis'),
    ('Machine Learning', 'Machine Learning'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Data Science', 'Data Science'),
    ('Web Development', 'Web Development'),
    ('Mobile App Development', 'Mobile App Development'),
    ('UI/UX Design', 'UI/UX Design'),
    ('Project Management', 'Project Management'),
    ('Agile/Scrum', 'Agile/Scrum'),
    ('Leadership', 'Leadership'),
    ('Communication Skills', 'Communication Skills'),
    ('Problem-solving', 'Problem-solving'),
    ('Teamwork', 'Teamwork'),
    ('Presentation Skills', 'Presentation Skills'),
    ('Networking', 'Networking'),
    ('Marketing', 'Marketing'),
    ('Sales', 'Sales'),
    ('Finance', 'Finance'),
    ('Accounting', 'Accounting'),
    ('Human Resources', 'Human Resources'),
    ('Digital Marketing', 'Digital Marketing'),
    ('Content Writing', 'Content Writing'),
    ('Graphic Design', 'Graphic Design'),
    ('Video Editing', 'Video Editing'),
    ('Photography', 'Photography'),
    ('Event Planning', 'Event Planning'),
    ('Foreign Languages', 'Foreign Languages'),
    ('Time Management', 'Time Management'),
    ('Customer Service', 'Customer Service'),
    ('Public Speaking', 'Public Speaking'),
    ('Research', 'Research'),
    ('Critical Thinking', 'Critical Thinking'),
    ('Presentation Design', 'Presentation Design'),
    ('Microsoft Office Suite', 'Microsoft Office Suite'),
    ('Google Suite', 'Google Suite'),
    ('Project Coordination', 'Project Coordination'),
    ('Social Media Management', 'Social Media Management'),
    ('Product Management', 'Product Management'),
    ('Quality Assurance', 'Quality Assurance'),
    ('DevOps', 'DevOps'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Network Security', 'Network Security'),
)

class Skill(models.Model):
    skill = models.CharField(max_length=30, choices=SKILL_CHOICES, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

    class Meta:
        unique_together = ("skill", "user")

INTEREST_CHOICES = (
    ("Array", "Array"),
    ("String", "String"),
    ("Linked List", "Linked List"),
    ("Tree", "Tree"),
    ("Graphs", "Graphs"),
    ("Dynamic Programming", "Dynamic Programming"),
    ("Backtracking", "Backtracking"),
    ("Stack", "Stack"),
    ("Queue", "Queue"),
    ("Heap", "Heap"),
    ("Hash Table", "Hash Table"),
    ("Sorting and Searching", "Sorting and Searching"),
    ("Bit Manipulation", "Bit Manipulation"),
    ("Greedy", "Greedy"),
    ("Math", "Math"),
    ("Geometry", "Geometry"),
    ("Randomization", "Randomization"),
    ("Simulation", "Simulation"),
    ("Design", "Design"),
    ("Object-Oriented Design", "Object-Oriented Design"),
    ("Concurrency", "Concurrency"),
    ("Operating System", "Operating System"),
    ("Database", "Database"),
    ("System Design", "System Design"),
    ("Network", "Network"),
    ("Web Development", "Web Development"),
    ("Machine Learning", "Machine Learning"),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Computer Vision", "Computer Vision"),
    ("Natural Language Processing", "Natural Language Processing"),
    ("Data Science", "Data Science"),
    ("Big Data", "Big Data"),
    ("Cloud Computing", "Cloud Computing"),
    ("Blockchain", "Blockchain"),
    ("Cybersecurity", "Cybersecurity"),
    ("Digital Signal Processing", "Digital Signal Processing"),
    ("Image Processing", "Image Processing"),
    ("Signal Processing", "Signal Processing"),
    ("Audio Processing", "Audio Processing"),
    ("Video Processing", "Video Processing"),
    ("Game Development", "Game Development"),
    ("Virtual Reality", "Virtual Reality"),
    ("Augmented Reality", "Augmented Reality"),
    ("Mobile Development", "Mobile Development"),
    ("Desktop Development", "Desktop Development"),
    ("Embedded Systems", "Embedded Systems"),
    ("Robotics", "Robotics"),
    ("IoT", "IoT"),
    ("Microservices", "Microservices"),
    ("Serverless Computing", "Serverless Computing"),
    ("CI/CD", "CI/CD"),
    ("DevOps", "DevOps"),
    ("Testing", "Testing"),
    ("Debugging", "Debugging"),
    ("Code Review", "Code Review"),
    ("Code Quality", "Code Quality"),
    ("Code Optimization", "Code Optimization"),
    ("Scalability", "Scalability"),
    ("Performance", "Performance"),
    ("Security", "Security"),
    ("Privacy", "Privacy"),
    ("Accessibility", "Accessibility"),
    ("Internationalization", "Internationalization"),
    ("Localization", "Localization"),
    ("Technical Writing", "Technical Writing"),
    ("Documentation", "Documentation"),
    ("Project Management", "Project Management"),
    ("Agile Methodology", "Agile Methodology"),
    ("Leadership", "Leadership"),
    ("Teamwork", "Teamwork"),
    ("Communication", "Communication"),
    ("Presentation Skills", "Presentation Skills"),
    ("Interview Preparation", "Interview Preparation"),
    ("Career Development", "Career Development"),
    ("Entrepreneurship", "Entrepreneurship"),
    ("Finance", "Finance"),
    ("Marketing", "Marketing"),
    ("Product Management", "Product Management"),
    ("Sales", "Sales")
)

class Interest(models.Model):
    interest = models.CharField(max_length=40, choices=INTEREST_CHOICES, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.interest

    class Meta:
        unique_together = ("interest", "user")
    
class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    interview_date = models.DateField()
    requesting_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviewee")
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviewer")
    rating = models.IntegerField(default=0)
    review = models.TextField()
