# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 07:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weather', '0004_auto_20180523_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCity',
            fields=[
                ('favorite_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.City', verbose_name='Город')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Избранные города',
                'verbose_name': 'Избранный город',
            },
        ),
    ]
