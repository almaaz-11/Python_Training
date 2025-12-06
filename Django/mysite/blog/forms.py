from django import forms
from .models import Post   # make sure Post model exists in models.py

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]   # adjust based on your Post model fields
