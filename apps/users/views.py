from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SkillUpdateForm, InterestUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, Profile, Interest
from django.contrib.auth.views import LoginView
#from .matching import match_users


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
    profiles = Profile.objects.exclude(user=request.user)
    skills_lists = []
    for profile in profiles:
        skills = Skill.objects.filter(user=profile.user)
        skills_lists.append(list(skills))

    results = zip(profiles, skills_lists)
    context = {
        "results" : results,
    }
    return render(request, 'connect.html', context)

@login_required
def follow_user(request):
    return
