from django.urls import path
from . import views

app_name = 'usersApp'

urlpatterns = [
    path('login/', views.login, name='login')
]