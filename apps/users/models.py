from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(4)], null=True, blank=True)
    student_status = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    calendly_link = models.URLField(blank=True)

    
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

    
class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    date_followed = models.DateField(default=timezone.now)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')

    def __str__(self):
        return f"{self.follower}, follows {self.following}"