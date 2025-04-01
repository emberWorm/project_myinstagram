from django import forms
from . import models

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'body', 'video']
        labels = { 
            "image": "Картинка",
            "body": "Подпись",
            "video": "Видео",
            }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'post-text', 'placeholder':'You can write something...'}),
        }
