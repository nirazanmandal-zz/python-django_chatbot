from django import forms
from .models import *


class RegisterUser(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['name', 'email', 'username', 'password']


class LoginUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
