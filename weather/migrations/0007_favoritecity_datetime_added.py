# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-29 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_auto_20180525_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritecity',
            name='datetime_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
