from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE),
#     avatar = models.ImageField(upload_to='users_avatars', blank=True, default='def_ava.jpeg')