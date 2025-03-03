from django import forms
from django.contrib.auth.forms import AuthenticationForm

class MyLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-b'})),
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-b'}))
    pass



# "В Django стандартные формы, такие как AuthenticationForm, не используют словарь widgets напрямую для установки виджетов полей."

# 'в случае с формой AuthenticationForm, которая не связана напрямую с какой-либо моделью, класс Meta не обязателен.'