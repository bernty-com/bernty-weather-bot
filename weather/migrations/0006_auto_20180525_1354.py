# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_favoritecity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecity',
            name='favorite_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
