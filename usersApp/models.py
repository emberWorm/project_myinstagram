from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='users_avatars', blank=True, default='users_avatars/def_ava.jpg')
    bio = models.CharField(max_length=150)