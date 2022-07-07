from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            cd = user_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)
            return redirect("catalog")
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form,'title':'Регистрация'})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,f'{user.username}, добро пожаловать!!!')
                    return redirect('home')
                else:
                    messages.error(request,'Нет такого пользователя')
            else:
                messages.error(request,"неправильный логин или пароль")
    else:
        form = LoginForm()
    return render(request, 'account/log_in.html', {'form': form,'title':'Вход'})


def user_logout(request):
    logout(request)
    return redirect("home")