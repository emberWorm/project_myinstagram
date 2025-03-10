from django.urls import path
from . import views

app_name = 'usersApp'

urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('reg/', views.register, name="sign_up"),
    path('<str:username>/', views.jopa, name="user_prof"),
]