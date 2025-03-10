from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from usersApp.models import UserProfile




@login_required(login_url='users:log_in')
def home(request):
    all_posts = models.Post.objects.all()


    context = {
        "all_posts":all_posts,
        }

    return render(request, 'generalApp/home.html', context)

@login_required(login_url='users:log_in')
def profile(request):
    user_id = request.user.id
    posts_user = models.Post.objects.filter(author_id=user_id)
    post_count = posts_user.count()

    # получаем профиль авторизированного пользователя
    # который из другого приложения
    user_profile = UserProfile.objects.get(user=request.user)

    print("ВНИМАНИЕ")
    print(user_profile)

    print(request)
    context = {
        "posts_user":posts_user,
        "post_count":post_count,
        # "all_posts":models.Post.objects.all()
        "profile":user_profile,
               }
    return render(
        request, 'generalApp/profile_last_ver.html', context)

def insta_post(request, pk):
    my_post = models.Post.objects.get(pk=pk)
    context = {
        "post":my_post,
    }
    return render(request, 'generalApp/post.html', context)

@login_required(login_url='users:log_in')
def create_post(request):
    form = forms.PostCreateForm() # обязательно ли () - ?

    message = '' # объявляем переменную чтобы не было исключений

    if request.method == "POST":
        
        form = forms.PostCreateForm(request.POST,request.FILES) # насколько я помню он славливает ее не сохраняя
        if form.is_valid():

            # присваивание авторства поста
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # title = form.cleaned_data['title'] 
            # body = form.cleaned_data['body']
            # image = form.cleaned_data['image']

            # # Данные в cleaned_data уже прошли все проверки is_valid() (заполнение, тип, формат даты..)

            # if models.Post.objects.filter(title=title).exists():
            # # title=title вытащи среди всех названий постов имя этого
            # # exists() - дает результат bool

            #     post = models.Post.objects.get(title=title)
            #     post.body = body
            #     post.image = image
            #     post.save() #---?

            #     message = 'поскольку был пост, обновлен былЪ'
            #     # messages.info(request, 'Пост с таким названием уже сущетсвует') - для админки

            # else:
            #     form.save()

            return redirect('generalApp:url_profile')

        
    context = {
        "form": form,
        "message":message,
    }
        
    return render (request, 'generalApp/create_post.html', context)

                # models.Post.objects.create(title=title, body=body, image=image)

def responsa(request):
    return JsonResponse({
        'lat':28
    })

@login_required(login_url='users:log_in')
def explore(request):
    # бог рандома
    explore_posts = models.Post.objects.all().order_by('?')
    context = {"explore_posts":explore_posts}
    return render(request, 'generalApp/explore.html', context)