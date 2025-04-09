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
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    # @property
    # def thumbnail(self):
    #     # Проверяем кэш
    #     # if cached := cache.get(f'post_{self.id}_thumb'):
    #         # return cached

    #     # Генерируем и сохраняем в кэш
    #     thumbnail_url = self._generate_thumbnail()
    #     # cache.set(f'post_{self.id}_thumb', thumbnail_url, 3600*24)  # Кэш на 24 часа
    #     return thumbnail_url

    # def _generate_thumbnail(self):
    #     if self.image:
    #         return self.image.url

    #     print('///////////////////////')
    #     # Для видео
    #     print(cv2.__version__)

    #     cap = cv2.VideoCapture(self.video.path)
    #     success, frame = cap.read()
    #     if success:
    #         # Сохраняем миниатюру в media/thumbnails
    #         thumb_path = f'thumbnails/{self.video.name}_thumb.jpg'
    #         cv2.imwrite(thumb_path, frame)
    #         return f'/media/{thumb_path}'
    #     return f'/static/generalApp/default_thumb.jpg'

    @property
    def thumbnail(self):
        """Свойство превью для облегченной загрузки Notifications"""

        # if not hasattr(self, '_thumbnail_url'):
        #     print(f"ГЕНЕРАЦИЯ ДЛЯ ОБЪЕКТА {id(self)}")
        #     """! объекты моделей в Django создаются заново при каждом запросе !"""

                    # # print(dir(self))
            # print('ГЕНЕРАЦИЯ МИНИАТЮРЫ')
            # # self._thumbnail_url = self._generate_thumbnail()

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

# class Comment(models.Model):
#     body = models.TextField()
#     when_added = models.DateTimeField(default=datetime.now)
#     author = models.ForeignKey(User)