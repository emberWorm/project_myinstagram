from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='url_home'),
    path('profile/', views.profile, name='url_profile'),
    # path('post/', views.insta_post),
    path('post/<int:pk>/', views.insta_post, name="view_post"),
    path('create/', views.create_post, name="url_create_post" )
]

# а как сделать 800/admin/?
# получается всегда все страницы в одном режиме просто 
# if user.auth