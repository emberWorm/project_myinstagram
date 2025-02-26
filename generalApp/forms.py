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
            'image': forms.FileInput(attrs={'class': 'photo-input'}),
            'body': forms.Textarea(attrs={'class': 'textarea-input'}),
        }