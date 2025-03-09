from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from . import forms

def log_in(request):
    form = forms.MyLoginForm(data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request,user)

        return redirect('generalApp:url_home')

    return render(request, 'usersApp/login.html', {'form': form})


def register(request):
    reg_form = forms.MyRegisterForm(data=request.POST or None)
    profile_form = forms.MyProfileForm(data=request.POST or None)

    if reg_form.is_valid() and profile_form.is_valid():
        user = reg_form.save()
        # profile form не понимает к какому юзеру привязываться, он не указан
        profile = profile_form.save(commit=False) # возвращает экземпляр модели с user = null

        profile.user = user # ссылка на объект юзера ведь в модели у нас он и принимает объект
        
        profile.save()

        return redirect('usersApp:log_in')
    
    context = {'reg_form':reg_form, 'profile_form':profile_form}
    
    return render(request, 'usersApp/sign_up.html', context)