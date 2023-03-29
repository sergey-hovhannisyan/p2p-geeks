from django.shortcuts import render
from django.http import HttpResponse
import os

parent_dir = os.path.dirname(os.getcwd())

def home(request):
    return render(request, os.path.join(parent_dir, "frontend\index.html"))
