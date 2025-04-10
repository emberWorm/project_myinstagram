from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from usersApp.models import UserProfile

from django.db.models import Q

from django.template.response import TemplateResponse

from django.http import JsonResponse

from datetime import datetime

from django.http import HttpResponse

from PIL import Image
# import subprocess
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# def base(request):
#     q = request.GET.get("q")

#     if q:
#        users_q = models.User.objects.filter(Q(username__icontains=q))

#     context = {'variable': 'значение'}
#     return TemplateResponse(request, 'generalApp/base_layout.html')


@login_required(login_url="users:log_in")
def home(request):
    all_posts = models.Post.objects.all().order_by("-when_added")

    context = {
        "all_posts": all_posts,
    }

    return render(request, "generalApp/home.html", context)


@login_required(login_url="users:log_in")
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
        "posts_user": posts_user,
        "post_count": post_count,
        # "all_posts":models.Post.objects.all()
        "profile": user_profile,
    }
    return render(request, "generalApp/profile_last_ver.html", context)


@login_required(login_url="users:log_in")
def insta_post(request, pk):
    my_post = models.Post.objects.get(pk=pk)
    # time_display = my_post.when_added.date()
    time_display = my_post.when_added
    # формат настроен в LANGUAGE_CODE = 'en-us', USE_I18N = True-?
    # (django/conf/locale/<locale>/formats.py).

    # Проверяем, AJAX-ли это запрос Чтобы можно было пререходить по прямой ссылке
    if request.headers.get("X-Request-With") == "Fetch":
        template = "generalApp/post_modal_n.html"  # Только контент модалки
    else:
        template = "generalApp/post.html"

    # now_time = datetime.now()
    # time_diff = now_time - time_display

    # print("ВНИМАНИЕ")

    # print(time_diff)

    context = {
        "post": my_post,
        "time_display": time_display,
    }
    return render(request, template, context)


@login_required(login_url="users:log_in")
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    if request.user == post.author:
        post.delete()
    else:
        print("DEBUG НЕТУ КАРОЧЕ НЕ ТОТ ЮЗЕР")
    # return redirect('generalApp:user_prof', username=request.user.username)
    htprespone = HttpResponse()
    print("WARNING /////")
    print(htprespone)
    print("///// WARNING")
    return HttpResponse()


def handle_uploaded_image(image):
    """Обрезка изображения до соотношения 1:1."""
    img = Image.open(image)
    width, height = img.size
    size = min(width, height)
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2
    img = img.crop((left, top, right, bottom))

    # Сохранение обрезанного изображения
    output = BytesIO()
    img.save(output, format="JPEG", quality=90)
    output.seek(0)
    return InMemoryUploadedFile(
        output, "ImageField", image.name, "image/jpeg", output.tell(), None
    )


@login_required(login_url="users:log_in")
def create_post(request):
    form = forms.PostCreateForm()  # обязательно ли () - ?

    message = ""  # объявляем переменную чтобы не было исключений

    if request.method == "POST":

        form = forms.PostCreateForm(
            request.POST, request.FILES
        )  # насколько я помню он славливает ее не сохраняя
        if form.is_valid():

            if "image" in request.FILES:
                image_file = handle_uploaded_image(request.FILES["image"])
                form.instance.image = image_file  # Присваиваем обработанное изображение

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

            return redirect("generalApp:url_profile")

    context = {
        "form": form,
        "message": message,
    }

    return render(request, "generalApp/create_post.html", context)

    # models.Post.objects.create(title=title, body=body, image=image)


def responsa(request):
    return JsonResponse({"lat": 28})


@login_required(login_url="users:log_in")
def explore(request):
    # бог рандома
    explore_posts = models.Post.objects.all().order_by("?")

    context = {"explore_posts": explore_posts}
    return render(request, "generalApp/explore.html", context)


def get_search_data(request):
    pass


def get_data_search(request):
    param = request.GET.get("param")

    search_users = models.User.objects.filter(
        Q(userprofile__name__icontains=param) | Q(username__icontains=param)
    )
    # i contains - ingnor case contains

    # json не принимает queryset поэтому его надо запарсить в список
    users_list = [
        {
            "username": bebra.username,
            "name": bebra.userprofile.name,
            "avatar_url": bebra.userprofile.avatar.url,
        }
        for bebra in search_users
    ]
    # я не думал что будет работаь с первого раза

    result_users = {"users": users_list}

    # data = {'key': 'Привет, это JSON-ответ из Django! ты ввел ' + param}

    return JsonResponse(result_users)


def post_like(request, post_id):
    post_data = models.Post.objects.get(pk=post_id)

    if request.user not in post_data.likes.all():
        post_data.likes.add(request.user)
    elif request.user in post_data.likes.all():
        post_data.likes.remove(request.user)

    post_likes = post_data.likes.count()

    return JsonResponse({"likes": post_likes})


def notifications(request):
    # user = request.user
    # TypeError: Object of type User is not JSON serializable
    user = request.user
    # posts_user = models.Post.likes.all()

    through_table = models.Post.likes.through
    fields = [field.name for field in through_table._meta.fields]
    print("Поля промежуточной таблицы:", fields)

    table_objects = through_table.objects.all()
    for obj in table_objects:
        print(
            f"запись {obj.id} пользователь {obj.user} лайкнул пост {obj.post} автора {obj.post.author}"
        )

    print("///////////////")

    author_objects = through_table.objects.filter(
        post__author__username=request.user.username
    )  # ну или author = user obj

    # вы пытаетесь post.author, но post — это поле ЧЕРЕЗ-таблицы, а не объект поста. Правильно использовать post__author.
    for obj in author_objects:
        # print(f'запись {obj.id} пользователь {obj.user} лайкнул пост {obj.post} автора ')
        print(obj.id, obj.user, obj.post.id)
    # fields = [field.name for field in author_objects.fields]
    # print(fields)

    notif_results = [
        {
            "username": like_event.user.username,
            "user_avatar_url":like_event.user.userprofile.avatar.url,
            "id_post": like_event.post.id,
            "thumbnail_url": like_event.post.thumbnail,
            # **(
            #     {"post_image_url": like_event.post.image.url} if like_event.post.image # and like_event.post.image.url
            #     else ({"post_video_url": like_event.post.video.url}  # if like_event.post.video and like_event.post.video.url else {}
            #     )
            # ),
        }
        for like_event in author_objects
    ]

    # print(notif_results)
    for result in notif_results:
        print(result)

    return JsonResponse({"likes_event": notif_results})
