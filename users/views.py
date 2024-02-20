from django.shortcuts import render, HttpResponseRedirect
from django.urls  import reverse

from users.forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib import auth
from users.models import User
from catalog.models import Busket


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


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:        
        form = UserProfileForm(instance=request.user)
    context = {
        "form": form,
        "title": "Профиль",
        "buskets": Busket.objects.filter(user=request.user)
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))