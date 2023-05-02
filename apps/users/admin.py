from django.contrib import admin
from .models import Profile, Skill, Interest, Interview

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Interview)
admin.site.register(Interest)