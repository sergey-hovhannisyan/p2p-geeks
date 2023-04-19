from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Skill
from ..posts.models import Author


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Author.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=User)
# def create_skill(sender, instance, created, **kwargs):
#     if created:
#         Skill.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_skill(sender, instance, **kwargs):
#     instance.skill.save()