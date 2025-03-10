from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from . import forms, models
from generalApp.models import Post
from django.contrib.auth.decorators import login_required

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