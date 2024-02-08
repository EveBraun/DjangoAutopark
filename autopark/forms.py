import datetime

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Driver, Car, CarBrand, Client
from AutoparkProject.settings import DATE_INPUT_FORMATS


# class DriverModelForm(forms.ModelForm):
#     class Meta:
#         model = Driver
#         exclude = ["is_available"]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        
        labels = {
        'username': 'Логин',
        'email': 'ПОЧТА',
        'password1' : 'Пароль',
        'password2' : 'Повторите пароль'
    }
        
        help_texts =  {
        'username': '',
        'password' : ''}

class DriverForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format='%d.%m.%Y'), input_formats='%d.%m.%Y')
    class Meta:
        model = Driver
        exclude = ['user', 'is_available']