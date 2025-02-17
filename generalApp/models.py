from django.db import models
from django.contrib.auth.models import User
# Class User - есть в джанго
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    body = models.CharField(max_length=1024) # потом поменяем
    author = models.ForeignKey( # id автора
        User,
        related_name='author',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None)
    when_added = models.DateTimeField(default=datetime.now)

class Followers(models.Model):
    # айдишник подписки (или как?)
    from_user = models.ForeignKey(# id юзера от
        User,
        related_name='from_user',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None)

    to_user = models.ForeignKey(# id юзера за кем наблюдаем (follow)
        User,
        related_name='to_user',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None)
    
    when_added = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Followers'
        verbose_name = 'FollOOWWWERRS'