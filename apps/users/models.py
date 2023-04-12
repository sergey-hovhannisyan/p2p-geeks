from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school_name = models.CharField(max_length=100, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    student_status = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    calendly_link = models.URLField(blank=True)

    
    def __str__(self):
        return self.username

class Skill_Set(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=20, blank=False)
    skill_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill
    
    class Meta:
        unique_together = ("skill", "user_id")

    
class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    date_followed = models.DateField(default=timezone.now)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_set')

    def __str__(self):
        return f"{self.follower}, follows {self.following}"