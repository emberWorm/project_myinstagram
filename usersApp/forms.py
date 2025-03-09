from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'input'}))
    
# "В Django стандартные формы, такие как AuthenticationForm, не используют словарь widgets напрямую для установки виджетов полей."

# 'в случае с формой AuthenticationForm, которая не связана напрямую с какой-либо моделью, класс Meta не обязателен.'

class MyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password', 'class':'input'}))

class MyProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['name']

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Name','class':'input'}))
    
    

