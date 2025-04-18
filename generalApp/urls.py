from django.urls import path
from . import views

app_name = 'generalApp'

urlpatterns = [
    path('', views.home, name='url_home'),
    # path('1/', views.responsa, name='url_responsa'),
    path('api/search/', views.get_data_search, name='url_responsa'),
    path('profile/', views.profile, name='url_profile'),
    path('post/<int:pk>/', views.insta_post, name="view_post"),
    path('create/', views.create_post, name="url_create_post" ),
    path('explore/', views.explore, name='explore'),
    path('post/<int:id>/delete/', views.delete_post, name="delete_post"),
    path('post_like/<int:post_id>/', views.post_like, name="post_like"),
    path('api/notifications/', views.notifications),
    path('api/create_comment/', views.create_comment),
    path('api/make_follow/', views.make_follow)
]
