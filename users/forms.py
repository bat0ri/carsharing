from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


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


    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите логин'
    }),)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Введите почту'
    }),)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'Пароль'
    }),)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 mb-4 bg-gray-200 text-white dark:bg-gray-800 border-b border-gray-600 focus:outline-none focus:border-blue-500',
        'placeholder': 'повторите Пароль'
    }),)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        # Отключаем валидацию email
        return self.cleaned_data['email']


