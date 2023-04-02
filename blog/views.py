from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    "author" : "nic\k",
    "title" : "Blog post 1",
    "content" : "firt post content",
    "date_posted" : "august 27"
    },
    {
    "author" : "Jange",
    "title" : "Blog post 2",
    "content" : "second post content",
    "date_posted" : "august 28"
    }
]

def home(request):
    context = {
        "posts" : posts, 
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title" : "about"})