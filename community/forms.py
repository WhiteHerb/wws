from django import forms
from django.views.decorators.csrf import csrf_exempt

from .models import Post

class PostForm(forms.ModelForm):

  @csrf_exempt
  class Meta:
    model=Post
    fields=('title','text',)