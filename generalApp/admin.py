from django.contrib import admin
from django.db.models import ManyToManyField, ForeignKey # здесь класс модели это из базы джанго а не из моих собственных
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Post._meta.get_fields() 
        if not isinstance(field, ManyToManyField) and not field.auto_created] 
    # для M2M не отображаем потому что вызывает ошибку потому что m2m возвращает таблицу (можно создать кастом функцию для колва лайков)
    

@admin.register(models.Followers)
class FollowersAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in models.Exchange._meta.get_fields()]
    pass
    # https://docs.djangoproject.com/en/5.1/ref/models/meta/#retrieving-all-field-instances-of-a-model

@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Comment._meta.get_fields()]


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass