from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SkillUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill


def register(request):
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

# @login_required
# def profile(request):
#     skill_set = Skill.objects.filter(user=request.user)
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         s_form = SkillUpdateForm(request.POST, user=request.user)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your profile has been updated!')
#             return redirect("profile") 
#         if s_form.is_valid():
#             s_form.save()

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#         s_form = SkillUpdateForm(user=request.user)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#         's_form': s_form,
#         'skill_set' : skill_set
#     }
#     return render(request, 'profile.html', context)




@login_required
def profile(request):
    skill_set = Skill.objects.filter(user=request.user)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    s_form = SkillUpdateForm(user=request.user)
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

    context = {
        'u_form': u_form,
        'p_form': p_form,
        's_form': s_form,
        'skill_set' : skill_set
    }
    return render(request, 'profile.html', context)
