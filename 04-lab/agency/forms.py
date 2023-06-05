from django import forms
from .models import Client, Package, Order
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


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ('name', 'country', 'hotels', 'price', 'duration')



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'address', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'package']
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['client'] = ClientForm()

