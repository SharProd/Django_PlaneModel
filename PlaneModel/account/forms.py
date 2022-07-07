from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150,min_length=4,label='Имя',widget=forms.TextInput({'class':'form-control','placeholder':'Имя пользователя'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput({'class':'form-control','placeholder':'Email адрес'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class':'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput({'class':'form-control','placeholder':'Пароль для подтверждения'}))

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         messages.error(request,'errors registration')
    #     return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,min_length=4,label='Имя',widget=forms.TextInput({'class':'form-control','placeholder':'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class':'form-control','placeholder':'Пароль'}))
