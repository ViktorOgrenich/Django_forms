from .models import News
from django.forms import ModelForm, TextInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'text', 'created_date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор статьи'
            }),
            "created_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публицации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }