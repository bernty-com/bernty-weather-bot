# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-23 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20180516_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='local_name',
            field=models.CharField(default='', max_length=100, verbose_name='Локальное название'),
        ),
    ]
