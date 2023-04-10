from django.shortcuts import render, redirect
from blog.models import Post 

def login(request):
    recent_post = Post.objects.all()[5:10]
    
    context = {
        'recent_post' : recent_post
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    recent_post = Post.objects.all()[5:10]
    
    context = {
        'recent_post' : recent_post
    }
    return render(request, 'accounts/register.html', context)
    

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
