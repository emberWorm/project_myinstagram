from django.db import models
from django.contrib.auth.models import User
# Class User - есть в джанго
from datetime import datetime
import cv2
from django.conf import settings
import os
from django.core.cache import cache


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='no title')
    image = models.ImageField(
        upload_to="users_posts_images",
        null=True, blank=True, # ВОТ ЭТО НАДО
        # default='default_photo.jpeg'
        )
    video = models.FileField(upload_to='post_videos/', null=True, blank=True) # ВОУ ВОУ
    body = models.CharField(max_length=1024, blank=True, default='') # потом поменяем
    author = models.ForeignKey( # id автора
        User,
        related_name='author',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None)
    when_added = models.DateTimeField(default=datetime.now)

    @property
    def thumbnail(self):
        """Свойство превью для облегченной загрузки Notifications"""

        # if not hasattr(self, '_thumbnail_url'):
        #     print(f"ГЕНЕРАЦИЯ ДЛЯ ОБЪЕКТА {id(self)}")
        #     """! объекты моделей в Django создаются заново при каждом запросе !"""
        
        if self.image:
            return self.image.url
        
        # Ключ кэша с ID поста
        cache_key = f'post_thumb_{self.id}'
    
        # Проверяем кэш
        if cached_url := cache.get(cache_key):
            print('БЕРЕМ ПРЕВЬЮХУ ИЗ КЭШИКА')
            return cached_url
    
        # Генерация и сохранение в кэш
        thumb_url = self._generate_thumbnail()
        cache.set(cache_key, thumb_url, 60*60*24) # Сутки хранится до перезагрузки

        return thumb_url

    def _generate_thumbnail(self):
        
        print('ЗАПУСК ГЕНЕРАЦИИ МИНИАТЮРЫ ВИДЕО')

        # путь
        video_path = self.video.path

        # Дирректория для миниатюр
        thumb_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
        os.makedirs(thumb_dir, exist_ok=True) # если нет создаем

        # Генерируем уникальное имя файла
        video_name = os.path.basename(self.video.name)
        thumb_name = f'{video_name}_thumb.jpg'
        thumb_path = os.path.join(thumb_dir, thumb_name)

        # Чтение и сохранение кадра
        cap = cv2.VideoCapture(video_path)
        success, frame = cap.read()

        if success and cv2.imwrite(thumb_path, frame):
            return f'{settings.MEDIA_URL}thumbnails/{thumb_name}'

class Followers(models.Model):

    from_user = models.ForeignKey(# id юзера от
        User,
        related_name='following',
        on_delete=models.CASCADE)

    to_user = models.ForeignKey(# id юзера за кем наблюдаем (follow)
        User,
        related_name='followers',
        on_delete=models.CASCADE)
    
    when_added = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ('from_user', 'to_user') 
        db_table = 'Followers'
        verbose_name = 'FollOOWWWERRS'

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    when_added = models.DateTimeField(default=datetime.now)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    when_added = models.DateTimeField(default=datetime.now)