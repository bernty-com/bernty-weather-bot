# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-08 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0008_auto_20180607_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city_id',
            new_name='id',
        ),
    ]
