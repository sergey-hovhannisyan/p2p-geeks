from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['school_name', 'gpa', 'student_status', 'bio']

class SkillUpdateForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(SkillUpdateForm, self).__init__(*args, **kwargs)
    
    def clean_skill(self):
        skill = self.cleaned_data.get('skill')
        if Skill.objects.filter(user=self.user, skill=skill).exists() or not skill:
            raise forms.ValidationError("This skill already exists.")
        return skill
    
    def save(self, commit=True):
        instance = super(SkillUpdateForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance