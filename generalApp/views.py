from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, 'generalApp/home.html')

def profile(request):
    context = {
        "post_count":models.Post.objects.count(),
        "all_posts":models.Post.objects.all()
               }
    return render(
        request, 'generalApp/profile.html', context)

def insta_post(request, pk):
    my_post = models.Post.objects.get(pk=pk)
    context = {
        "post":my_post,
    }
    return render(request, 'generalApp/post.html', context)