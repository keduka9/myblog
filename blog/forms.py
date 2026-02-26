from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'タイトルを入力' }),
            'content': forms.Textarea(attrs={'class': 'forms-control', 'placeholder': '本文を入力', 'rows': 8}),
        }