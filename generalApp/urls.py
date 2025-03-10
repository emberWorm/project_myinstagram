from django.urls import path
from . import views

app_name = 'generalApp'

urlpatterns = [
    path('', views.home, name='url_home'),
    path('1/', views.responsa, name='url_responsa'),
    path('profile/', views.profile, name='url_profile'),
    path('post/<int:pk>/', views.insta_post, name="view_post"),
    path('create/', views.create_post, name="url_create_post" ),
    path('explore/', views.explore, name='explore')
]
