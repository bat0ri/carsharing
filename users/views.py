from django.shortcuts import render, HttpResponseRedirect
from django.urls  import reverse, reverse_lazy

from users.forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib import auth
from users.models import User
from catalog.models import Busket
from django.contrib.auth.views import LoginView
from common.views import CommonTitleMixin

from django.views.generic.edit import CreateView, UpdateView


class UserLoginForm(CommonTitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('catalog:index')
    title = 'Вход'



class UserRegistrationView(CommonTitleMixin, CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    title = 'Регистрация'


class UserProfileView(CommonTitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["busket"] = Busket.objects.filter(user=self.object)
        return context
