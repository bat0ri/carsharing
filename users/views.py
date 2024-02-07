from django.shortcuts import render, HttpResponseRedirect
from django.urls  import reverse

from users.forms import LoginForm, RegisterForm
from django.contrib import auth
from users.models import User


# Create your views here.
def login(request):

    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('catalog:index'))
    else:
        form = LoginForm()

    context = {
        'title': 'Вход',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):

    form = RegisterForm()
    
    if request.method =='POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    
    context = {
        "title": "Регистрация",
        "form": form
    }
    return render(request, 'users/registration.html', context)