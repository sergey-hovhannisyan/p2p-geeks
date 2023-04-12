from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post-home")
#     else:
#         form = UserRegistrationForm()
#     return render(request, "../frontend/register.html", {"form" : form})

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post-home")
#     else:
#         form = UserCreationForm()
#     return render(request, "../frontend/register.html", {"form" : form})

def register(request):
    return render(request, "../frontend/register.html")
