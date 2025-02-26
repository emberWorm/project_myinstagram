from django.shortcuts import render, redirect
from . import models, forms


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

def create_post(request):
    form = forms.PostCreateForm()# обязательно ли () - ?

    if request.method == "POST":
        form = forms.PostCreateForm(request.POST,request.FILES) # насколько я помню он славливает ее не сохраняя
        if form.is_valid():
            form.save()
            return redirect('generalApp:url_profile')
        
    context = {
        "form": form
    }
        
    return render (request, 'generalApp/create_post.html', context)