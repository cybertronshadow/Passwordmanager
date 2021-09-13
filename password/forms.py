from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm  # this is used for post and request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class StoredPasswordForm(ModelForm):
    class Meta:
        model = StoredPassword
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, ** kwargs):
        super(CustomUserCreationForm, self).__init__(*args, ** kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password..'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'confirm password...'})
