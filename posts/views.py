from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts

# Create your views here.

def posts(request):
    return render(request, 'posts/posts.html')


def about(request):
    return render(request, 'posts/about.html')


def home(request):
    return render(request, 'posts/home.html')


def post_list(request):
    posts = Posts.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

