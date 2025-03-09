from django.urls import path
from . import views

app_name = 'usersApp'

urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('reg/', views.register, name="sign_up"),
]