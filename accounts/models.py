# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from weather.models import Country

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Досье'
        )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Страна'
        )
    location = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Город',
        )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='День рождения',
        )
    email_confirmed = models.BooleanField(
        default=False,
        verbose_name='Email подтвержден',
        )


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()