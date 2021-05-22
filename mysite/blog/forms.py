from django import forms
from django.forms import ModelForm
from django.forms.widgets import Widget
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields = "__all__"
