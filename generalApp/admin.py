from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Post._meta.get_fields()]
    

@admin.register(models.Followers)
class FollowersAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in models.Exchange._meta.get_fields()]
    pass
    # https://docs.djangoproject.com/en/5.1/ref/models/meta/#retrieving-all-field-instances-of-a-model