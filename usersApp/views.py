from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from . import forms

def log_in(request):
    form = forms.MyLoginForm(data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request,user)

        return redirect('generalApp:url_home')

    return render(request, 'usersApp/indexlog.html', {'form': form})