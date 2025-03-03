from django import forms
from . import models

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','image', 'body']
        labels = { 
            "title": "Название поста",
            "image": "Картинка",
            "body": "Подпись"
            }
        # widgets = {
        #     'title':forms.CharField(),
        #     'image': forms.FileInput(attrs={'class': 'photo-input'}),
        #     'body': forms.Textarea(attrs={'class': 'textarea-input'}),
        # }