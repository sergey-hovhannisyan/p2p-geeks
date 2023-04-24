from django.contrib import admin
from .models import Profile, Skill, Interest, Follow

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Follow)
admin.site.register(Interest)