from django import forms
from . models import post,comment
class PostForm(forms.ModelForm):
    class Meta:
        model=post
        # fields='__all__'
        exclude = ['author']


class commentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=['name','email','body']
        