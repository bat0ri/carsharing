from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms

from users.models import User, EmailVerification
from users.tasks import send_email_verification
import uuid
from datetime import timedelta
from django.utils.timezone import now


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите логин'
    }),)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Пароль'
    }),)

    class Meta:
        model = User
        fields = ('username', 'password')


# n@3gPhFF=pyZYSe
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 \
        border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите логин'
    }),)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 \
            border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите логин'
    }),)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 \
            border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите почту'
    }),)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 \
            border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Пароль'
    }),)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 border-b \
            border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'повторите Пароль'
    }),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        # Отключаем валидацию email
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-black  border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите Имя'
    }),)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-black  border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите логин',
        'readonly': True
    }),)
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-black  border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите почту',
        'readonly': True
    }),)

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-black  border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Фотка',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'image')