from django import forms
from .models import addPost

class AddPostForm(forms.ModelForm):
    class Meta:
        model = addPost
        fields = ['title','description','photos']