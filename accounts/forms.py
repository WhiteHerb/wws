from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class SignupForm(UserCreationForm):
  email = forms.EmailField(max_length=60, help_text='필수, 이메일을 입력하세요')
  username = forms.CharField(max_length=10, help_text='실제 이름으로 입력하세요') 
  stu_ID = forms.CharField(max_length=5, help_text='')
  class Meta:
    model = Account
    fields = ('email','username','schoolname','grade','stu_ID','password1','password2')
    