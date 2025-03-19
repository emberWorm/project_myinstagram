from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from . import forms, models
from generalApp.models import Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def log_in(request):
    form = forms.MyLoginForm(data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request,user)

        return redirect('generalApp:url_home')

    return render(request, 'usersApp/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('users:log_in')


def register(request):
    reg_form = forms.MyRegisterForm(data=request.POST or None)
    profile_form = forms.MyProfileForm(data=request.POST or None)

    if reg_form.is_valid() and profile_form.is_valid():
        user = reg_form.save()
        # profile form не понимает к какому юзеру привязываться, он не указан
        profile = profile_form.save(commit=False) # возвращает экземпляр модели с user = null

        profile.user = user # ссылка на объект юзера ведь в модели у нас он и принимает объект
        
        profile.save()

        return redirect('users:log_in')
    
    context = {'reg_form':reg_form, 'profile_form':profile_form}
    
    return render(request, 'usersApp/sign_up.html', context)

# тображение профилей всех юзеров
@login_required(login_url='users:log_in')
def jopa(request, username):
    user = models.User.objects.get(username=username)

    posts_user = Post.objects.filter(author_id=user.id)
    post_count = posts_user.count()

    if request.user.username == username:
        is_current_user = True
    else:
        is_current_user = False
    
    context = {
        'is_current_user': is_current_user,
        "posts_user":posts_user,
        "post_count":post_count,
        # "profile":user_profile,
        "user":user
               }
    
    return render(
        request, 'generalApp/profile_last_ver.html', context)
        # request, 'generalApp/PROFILENEW.html', context)

@login_required(login_url='users:log_in')
def edit_profile(request, username):

    user = models.User.objects.get(username=username)

    userprofile = models.UserProfile.objects.get(user_id=user.id)
    form_ed_p = forms.EditProfileForm(request.POST or None, request.FILES or None, instance=userprofile)
    form_ed_usr = forms.EditUsernameForm(request.POST or None, instance=user)

    print("ABOBA")
    print(userprofile)

    # form = forms.MyProfileForm(request.POST or None, request.FILES or None, instance=post_data)
    if form_ed_p.is_valid() and form_ed_usr.is_valid():
        form_ed_p.save()
        form_ed_usr.save()

        # во избежание ошибок  с перенаправлением используем функ reverse() которая создает url с параметрами
        new_username = user.username
        return redirect(reverse('users:profile_edit', kwargs={'username': new_username})) # keyword agrs именованные а не позиционные
    
        # Если обычная маршрутизация — это процесс "входа" (URL → представление), то reverse() — это процесс "выхода" (представление/маршрут → URL)

        # return redirect(request.path)
        # return redirect(reverse('profile_edit', kwargs={'user_id': user.id}))


    context = {"user":user, "form_ed_p":form_ed_p, 'form_ed_usr':form_ed_usr}
    return render(request, 'generalApp/edit-profile.html', context)