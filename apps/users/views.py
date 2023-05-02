from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SkillUpdateForm, InterestUpdateForm, ReviewForm, ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, Profile, Interest, Interview
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .matching import match_users
import datetime

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        view = LoginView.as_view(template_name="login.html")
        return view(request)

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("profile") 
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form" : form})


@login_required
def profile(request):
    skill_set = Skill.objects.filter(user=request.user)
    interest_set = Interest.objects.filter(user=request.user)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    s_form = SkillUpdateForm(user=request.user)
    i_form = InterestUpdateForm(user=request.user)
    if request.method == 'POST':
        if 'profile_update' in request.POST:  # Check if profile update form submitted
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your profile has been updated!')
                return redirect("profile")
        elif 'skill_update' in request.POST:  # Check if skill update form submitted
            s_form = SkillUpdateForm(request.POST, user=request.user)
            if s_form.is_valid():
                s_form.save()
            else:
                messages.warning(request, f'Skill already exists!')
                return redirect("profile")
        elif 'interest_update' in request.POST:  # Check if interest update form submitted
            i_form = InterestUpdateForm(request.POST, user=request.user)
            if i_form.is_valid():
                i_form.save()
            else:
                messages.warning(request, f'Interest already exists!')
                return redirect("profile")

    context = {
        'u_form': u_form,
        'p_form': p_form,
        's_form': s_form,
        'i_form': i_form,
        'skill_set' : skill_set,
        'interest_set' : interest_set,
    }
    return render(request, 'profile.html', context)

@login_required
def connect(request):
    current_profile = Profile.objects.filter(user=request.user).first()
    profiles = match_users(current_profile)
    skills_lists = []
    interest_lists = []
    for profile in profiles:
        skills = Skill.objects.filter(user=profile.user)
        interests = Interest.objects.filter(user=profile.user)
        skills_lists.append(list(skills))
        interest_lists.append(list(interests))

    results = zip(profiles, skills_lists, interest_lists)
    context = {
        "results" : results,
    }

    if request.method == "POST":
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('schedule')

    return render(request, 'connect.html', context)

@login_required
def review(request):
    print()
    id = request.session.get('id')
    print("INTERVIEW ID ", id)
    interview = Interview.objects.get(id=id)

    form = ReviewForm(request.POST or None, instance=interview)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, f'Your review was sent!')
            return redirect('interviews')
        else:
            messages.warning(request, f'Rating is on a scale from 0-5.')
            return redirect("review")
        
    return render(request, "review.html", {"form": form})

@login_required
def interviews(request):
    today = datetime.date.today()
    next_year = today.replace(year=today.year + 1)
    old = today.replace(year=today.year - 2)

    upcoming = Interview.objects.filter(requesting_user=request.user, interview_date__range=[str(today), str(next_year)])
    upcoming2 = Interview.objects.filter(interviewer=request.user, interview_date__range=[str(today), str(next_year)])
    upcoming_list = list(upcoming)
    upcoming_list += list(upcoming2)

    past_interviews = Interview.objects.filter(requesting_user=request.user, interview_date__range=[str(old), str(today)])
    past_meetings = list(past_interviews)

    meeting_to_review = Interview.objects.filter(interviewer=request.user, interview_date__range=[str(old), str(today)])
    to_review = list(meeting_to_review)

    context = {
        "upcoming_list": upcoming_list,
        "past_meetings": past_meetings,
        "to_review": to_review,
    }

    if request.method == "POST":
        id = request.POST.get('id')
        request.session['id'] = id
        return redirect('review')

    return render(request, "interviews.html", context)

@login_required
def schedule(request):
    print()
    username = request.session.get('username')
    interviewer = User.objects.get(username=username)
    
    initial = {
        'requesting_user': request.user,
        'interviewer': interviewer,
    }
    print("Initial: ", initial)

    form = ScheduleForm(request.POST or None, initial=initial)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('interviews')
        
    return render(request, "schedule.html", {"form": form})

def handler404(request, exception):
    return render(request, '404.html', status=404)