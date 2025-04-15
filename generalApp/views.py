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

import json
import itertools


# import subprocess
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.shortcuts import get_object_or_404

# def base(request):
#     q = request.GET.get("q")

#     if q:
#        users_q = models.User.objects.filter(Q(username__icontains=q))

#     context = {'variable': 'значение'}
#     return TemplateResponse(request, 'generalApp/base_layout.html')


@login_required(login_url="users:log_in")
def home(request):
    all_posts = models.Post.objects.all().order_by("-when_added")

    # posts_followed_users = models.Post.objects.filter(author=request.user.following )
    # posts_followed_users = models.Post.objects.filter(author__in=[f.following for f in request.user.following.all()])

    users_not_followed = models.User.objects.exclude(id__in=request.user.following.values('to_user')).order_by("?")
    users_not_followed_slice = users_not_followed[:3]

    users_followed_ids= models.User.objects.filter(id__in = request.user.following.values('to_user'))
    # request.user.following.values('to_user') словарь с ключом to_user
    ids_plus_req_user = list(users_followed_ids) + [request.user.id]
    posts_followed_users = models.Post.objects.filter(author__in=ids_plus_req_user).order_by("-when_added")

    liked_post_ids = models.Like.objects.filter(
        user=request.user,
        post__in=posts_followed_users
    ).values_list('post_id', flat=True)

    context = {
        "all_posts": posts_followed_users,
        'users_followed':users_followed_ids,
        'liked_post_ids':liked_post_ids,
        'users_not_followed_slice':users_not_followed_slice,
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

    is_liked = models.Like.objects.filter(user=request.user, post=my_post).exists()
    
    context = {
        "post": my_post,
        "time_display": time_display,
        'is_liked':is_liked,
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

    # if request.user not in post_data.likes.all():

    #     post_data.likes.add(request.user)
    # elif request.user in post_data.likes.all():
    #     post_data.likes.remove(request.user)

    like_obj, created = models.Like.objects.get_or_create(
        user=request.user, post=post_data
    )

    if not created:
        like_obj.delete()

    post_likes = post_data.like_set.count()

    return JsonResponse({"likes": post_likes})


def notifications(request):
    # user = request.user
    # TypeError: Object of type User is not JSON serializable
    # user = request.user
    # posts_user = models.Post.likes.all()

    # fields = [field.name for field in through_likes_table._meta.fields]
    # print("Поля промежуточной таблицы:", fields)

    # table_objects = through_likes_table.objects.all()
    # for obj in table_objects:
    #     print(
    #         f"запись {obj.id} пользователь {obj.user} лайкнул пост {obj.post} автора {obj.post.author}"
    #     )

    # print("///////////////")

    # comments_table = models.Comment.objects.filter(post_)

    # author_objects = through_likes_table.objects.filter(
    #     post__author__username=request.user.username
    # )  # ну или author = user obj

    # вы пытаетесь post.author, но post — это поле ЧЕРЕЗ-таблицы, а не объект поста. Правильно использовать post__author.
    # for obj in author_objects:

    # print(f'запись {obj.id} пользователь {obj.user} лайкнул пост {obj.post} автора ')
    # print(obj.id, obj.user, obj.post.id)

    # fields = [field.name for field in author_objects.fields]
    # print(fields)

    req_user_followers = list(models.Followers.objects.filter(to_user=request.user))

    req_user_comment = list(models.Comment.objects.filter(post__author=request.user))

    req_user_likes = list(models.Like.objects.filter(post__author=request.user))

    all_event_objects = itertools.chain(
        req_user_followers, req_user_comment, req_user_likes
    )

    print(all_event_objects)

    sort_obj_data = sorted(all_event_objects, key=lambda x: x.when_added, reverse=True)

    print(sort_obj_data)

    serialized_events = []
    for event in sort_obj_data:
        if isinstance(event, models.Followers):
            serialized_events.append(
                {
                    "type": "follow",
                    "user": event.from_user.username,
                    "avatar_url": event.from_user.userprofile.avatar.url,
                    "date": event.when_added,
                    "message": f"started following you.",
                }
            )
        elif isinstance(event, models.Comment):
            serialized_events.append(
                {
                    "type": "comment",
                    "user": event.author.username,
                    "avatar_url": event.author.userprofile.avatar.url,
                    "post_id": event.post.id,
                    "thumbnail_url": event.post.thumbnail,
                    "text": event.body[:20],
                    "date": event.when_added,
                    "message": f'commented on your post: {event.body[:20]}...',
                }
            )
        elif isinstance(event, models.Like):
            serialized_events.append(
                {
                    "type": "like",
                    "user": event.user.username,
                    "avatar_url": event.user.userprofile.avatar.url,
                    "post_id": event.post.id,
                    "thumbnail_url": event.post.thumbnail,
                    "date": event.when_added,
                    "message": f'liked your post.',
                }
            )

    return JsonResponse({"events": serialized_events})


def create_comment(request):
    body_comment = request.POST.get("comment_text")
    author = request.user
    post_id_from_ajax = request.POST.get("postID")
    post = get_object_or_404(models.Post, id=post_id_from_ajax)

    # actual_comments = post.comment_set.all()
    # серка комментов
    # comments_data = [{'id': c.id, 'body': c.body, 'author': c.author.username}
    # for c in actual_comments]

    # body post author when
    insert_comment_object = models.Comment.objects.create(
        body=body_comment, post=post, author=author
    )

    insert_comment_dict = {
        "id": insert_comment_object.id,
        "avatar_url": insert_comment_object.author.userprofile.avatar.url,
        "body": insert_comment_object.body,
        "author": insert_comment_object.author.username,
    }

    a = [field.name for field in insert_comment_object._meta.get_fields()]

    return JsonResponse(
        {"на сервер пришло сообщение": a, "insert_comment": insert_comment_dict}
    )


def make_follow(request):
    data = json.loads(request.body)
    to_user_id = data.get("user_id")

    req_user = request.user

    user_to_follow = get_object_or_404(models.User, id=to_user_id)

    # if req_user not in user_to_follow.to_user.all(): что не так было?
    # ------------>
    # user_to_follow.followers.all() возвращает объекты Followers, а не пользователей.
    # Вы сравниваете объект User (req_user) с объектами Followers → условие всегда истинно.
    # ------------

    # if not models.Followers.objects.filter(from_user=req_user, to_user=user_to_follow).exists():
    #     models.Followers.objects.create(from_user=req_user, to_user=user_to_follow)
    #     return JsonResponse({f'Подписка from id {req_user.id} to id {to_user_id}': "Follow Успешно"})
    # else:
    #     models.Followers.objects.filter(from_user=req_user, to_user=user_to_follow).delete()
    #     return JsonResponse({f'Подписка from id {req_user.id} to id {to_user_id}': "Follow Удалена поскольку exists"})

    """Более современный вариант get_or_create - 1 запрос вместо 2х к бд"""
    follow_obj, created = models.Followers.objects.get_or_create(
        from_user=req_user, to_user=user_to_follow
    )

    if created:
        return JsonResponse(
            {
                f"Подписка from id {req_user.id} to id {to_user_id}": "Успешно",
                "Follow": "True",
            }
        )
    else:
        follow_obj.delete()
        return JsonResponse(
            {
                f"Подписка from id {req_user.id} to id {to_user_id}": "Удалена поскольку exists",
                "Follow": "False",
            }
        )
