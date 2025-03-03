from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required(login_url='users:login')
def home(request):
    all_posts = models.Post.objects.all()

    return render(request, 'generalApp/home.html', {"all_posts":all_posts})

@login_required(login_url='users:login')
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

@login_required(login_url='users:login')
def create_post(request):
    form = forms.PostCreateForm() # обязательно ли () - ?

    message = '' # объявляем переменную чтобы не было исключений

    if request.method == "POST":
        form = forms.PostCreateForm(request.POST,request.FILES) # насколько я помню он славливает ее не сохраняя
        if form.is_valid():
            title = form.cleaned_data['title'] # Данные в cleaned_data уже прошли все проверки is_valid() (заполнение, тип, формат даты..)
            body = form.cleaned_data['body']
            image = form.cleaned_data['image']
            if models.Post.objects.filter(title=title).exists():
                post = models.Post.objects.get(title=title)
                post.body = body
                post.image = image
                post.save() #---?

                message = 'поскольку был пост, обновлен былЪ'
                # messages.info(request, 'Пост с таким названием уже сущетсвует') - для админки

            # title=title вытащи среди всех названий постов имя этого
            # exists() - дает результат bool

            else:
                form.save()
                return redirect('generalApp:url_home')

        
    context = {
        "form": form,
        "message":message,
    }
        
    return render (request, 'generalApp/create_post.html', context)

                # models.Post.objects.create(title=title, body=body, image=image)
