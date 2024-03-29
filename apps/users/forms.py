from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Interest, Interview
from django.core.exceptions import ValidationError
import datetime

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
        fields = ['calendly_link', 'zoom_meeting_link', 'bio', 'school_name', 'student_status', 'gpa']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

    def clean_calendly_link(self):
        link = self.cleaned_data['calendly_link']
        check = "https://calendly.com/"
        if link[:len(check)] != check:
            raise forms.ValidationError(message='That is not a valid calendly!')
        return link


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

    
class InterestUpdateForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['interest']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(InterestUpdateForm, self).__init__(*args, **kwargs)
    
    def clean_interest(self):
        interest = self.cleaned_data.get('interest')
        if Interest.objects.filter(user=self.user, interest=interest).exists() or not interest:
            raise forms.ValidationError("This interest already exists.")
        return interest
    
    def save(self, commit=True):
        instance = super(InterestUpdateForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['rating', 'review']

class DateInput(forms.DateInput):
    input_type = 'date'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['interview_date', 'requesting_user', 'interviewer']
        widgets = {
            'interview_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["requesting_user"].disabled = True
        self.fields["interviewer"].disabled = True
    
    def clean_interview_date(self):
        date = self.cleaned_data['interview_date']
        if date < datetime.date.today():
            raise forms.ValidationError(message='That is not a valid date')
        return date


