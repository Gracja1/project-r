from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms


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


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return render(request, 'posts/signedup.html', {'user': user})
    else:

        form = UserCreationForm()
    return render(request, 'posts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return render(request, 'posts/loggedin.html', {'user': user})
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:8000/post-list/#')


@login_required(login_url="http://127.0.0.1:8000/login/")
def comment_view(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            # save to db
            return redirect('http://127.0.0.1:8000/post-list/#')
    else:
        form = forms.CreateComment()
    return render(request, 'posts/comment.html', {'form': form})
