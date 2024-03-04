from django.shortcuts import render, HttpResponseRedirect
from django.urls  import reverse, reverse_lazy
from django.views.generic.base import TemplateView

from users.forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib import auth
from users.models import User, EmailVerification
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

class EmailVerificationView(CommonTitleMixin, TemplateView):
    title = "Подтверждение электронной почты"
    template_name = 'users/verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verify = EmailVerification.objects.filter(code=code, user=user)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verify_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

