from django.shortcuts import render
from .models import Post, Comment

def home(request):
    context = {
        "posts" : Post.objects.all(),
        "comments" : Comment.objects.all(), 
    }
    return render(request, "frontend/feed.html", context)