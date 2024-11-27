from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *


class SignUpForm(UserCreationForm):
    fio = forms.CharField(widget=forms.TextInput, label='ФИО', help_text='Только буквы кириллицы, дефис и пробелы',
                          validators=[RegexValidator('^[а-яА-ЯёЁ-]+\s+[а-яА-ЯёЁ-]+\s+[а-яА-ЯёЁ-]', message="Неправильное ФИО, пожалуйста, введите корректные данные и  попробуйте снова.")],
                          required=True)
    username = forms.CharField(label='Логин', widget=forms.TextInput, help_text='Только латиница и дефис, уникальный', required=True,
                               validators=[RegexValidator('^[a-zA-Z-]', message = "Неправильный логин, пожалуйста, попробуйте снова.")],
                               error_messages={
                                   'unique': 'Этот логин уже занят другим пользователем,пожалуйста, попробуйте другой'
                               })
    email = forms.EmailField(label='Email', widget=forms.EmailInput, help_text='Валидный формат email-адреса', required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput, required=True)
    agree = forms.BooleanField(label='Согласие на обработку персональных данных', widget=forms.CheckboxInput, required=True)

    class Meta:
        model = UserProfile
        fields = ('fio', 'username', 'email', 'password1', 'password2','agree')


    def clean_password2(self):
        value = self.cleaned_data
        if value['password1'] != value['password2']:
            raise forms.ValidationError("Ошибка! Пароли не совпадают!")
        return value['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("Ошибка! Такой E-mail уже существует!")
        return email
