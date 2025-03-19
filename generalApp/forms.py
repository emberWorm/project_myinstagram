from django import forms
from . import models

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'body']
        labels = { 
            "image": "Картинка",
            "body": "Подпись"
            }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'post-text', 'placeholder':'You can write something...'}),
        }
