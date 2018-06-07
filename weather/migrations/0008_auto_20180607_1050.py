# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-07 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_favoritecity_datetime_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='weather.Country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='favoritecity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='weather.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='favoritecity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
