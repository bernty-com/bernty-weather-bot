# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from datetime import datetime as d

from weather.models import Country


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        label=smart_text('Адрес электронной почты'),
        help_text=smart_text('На адрес электронной почты будет отправлен запрос на подтверждение.')
        )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            )

    error_messages = {
        'empty_username':
            smart_text("Нехорошо как-то человеку без ника. Роботу можно."),
        'incorrect_location':
            smart_text("Ты с какова горада, %(first_name)s?"),
        'inactive_account':
            smart_text("Профиль пользователя не активирован."),
        'password_mismatch':
            smart_text("The two password fields didn't match."),

    }

#    def clean_username(self):
#        username = self.cleaned_data.get('username')
#        if username is None or username == '':
#            raise forms.ValidationError(
#                self.error_messages['empty_username'],
#                    code='empty_username',
#                )


def year_for_birth_date():
    year_now = d.now().year
    return tuple([int(_) for _ in range(year_now-80, year_now+1)])


class ProfileForm(forms.Form):
    first_name = forms.CharField(
        label=smart_text('Имя'),
        max_length=30,
        required=False,
        help_text=smart_text('Необязательное поле')
        )
    last_name = forms.CharField(
        label=smart_text('Фамилия'),
        max_length=30,
        required=False,
        help_text=smart_text('Необязательное поле')
        )
    email = forms.EmailField(
        max_length=254,
        label=smart_text('Адрес электронной почты'),
        widget=forms.EmailInput,
        help_text=smart_text('В случае изменения адреса будет отправлен повторный запрос на подтверждение.')
        )
    email_confirmed = forms.BooleanField(
        label=smart_text('Email подтвержден'),
        initial=False
        )
    birth_date = forms.DateField(
        label=smart_text('Дата рождения'),
        widget=forms.SelectDateWidget(years=year_for_birth_date()),
        help_text=smart_text('День рождения')
        )
    bio = forms.CharField(
        label=smart_text('Досье'),
        widget=forms.Textarea,
        max_length=500,
        required=False,
        help_text=smart_text('Дополнительная информация о клиенте'),
        )
    location = forms.CharField(
        label=smart_text('Город'),
        max_length=30,
        required=False,
        help_text=smart_text('Родной город'),
        )
    country = forms.ModelChoiceField(
        label=smart_text('Страна'),
        widget=forms.Select,
        queryset=Country.objects.all().order_by('name'),
        help_text=smart_text('Страна пребывания'),
        required=False,
        )

    error_messages = {
        'first_name':
            smart_text("Нехорошо как-то человеку без имени."),
        'incorrect_location':
            smart_text("Ты с какова горада, %(first_name)s?"),
        'inactive_account':
            smart_text("Профиль пользователя не активирован."),
    }

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'email_confirmed',
            'birth_date',
            'bio',
            'location',
            'country',
            )

#    def clean_first_name(self):
#        first_name = self.cleaned_data.get('first_name')
#        if first_name is None or first_name == '':
#            raise forms.ValidationError(
#                self.error_messages['first_name'],
#                code='first_name',
#                )

    def clean_location(self):
        first_name = self.cleaned_data.get('first_name')
        location = self.cleaned_data.get('location')
        if location == 'xxx':  # вот такая прихоть
            raise forms.ValidationError(
                self.error_messages['incorrect_location'],
                code='incorrect_location',
                params={'first_name': first_name},
                )
        return location
