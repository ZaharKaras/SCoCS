from django import forms
from .models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))

