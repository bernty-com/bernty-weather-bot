# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from .model_func import (
    day_duration,
    set_pressure,
    set_wind_direction,
    natural_time,
    coordinate,
    set_condition
)

from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation
from fav.models import Favorite


@python_2_unicode_compatible
class Country(models.Model):
    # Fields
    brief = models.CharField(
        max_length=10,
        primary_key=True,
        verbose_name='Код страны'
        )
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
        )

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    #  Fields
    id = models.IntegerField(
        primary_key=True,
        verbose_name="ID"
        )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
        )
    local_name = models.CharField(
        max_length=100,
        verbose_name='Локальное название',
        default=''
        )
    country = models.ForeignKey(
        'Country',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Страна',
        related_name='cities'
        )
    coord_lon = models.DecimalField(
        max_digits=19,
        decimal_places=6,
        verbose_name='Долгота'
        )
    coord_lat = models.DecimalField(
        max_digits=19,
        decimal_places=6,
        verbose_name='Широта'
        )
    favorites = GenericRelation(Favorite, related_query_name='cities')

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def get_absolute_url(self):
        return reverse('city.detail', args=[str(self.id)])

    def get_city_id(self):
        return self.city_id

    def __str__(self):
        return self.local_name if self.local_name != '' else self.name


class Forecast(models.Model):
    # Fields
    coord_lon = models.DecimalField(max_digits=19, decimal_places=6)
    coord_lat = models.DecimalField(max_digits=19, decimal_places=6)
    lon = models.CharField(max_length=11)
    lat = models.CharField(max_length=11)
    weather_id = models.IntegerField()
    weather_main = models.CharField(max_length=20)
    weather_description = models.CharField(max_length=50)
    weather_icon = models.CharField(max_length=10)
    temperature = models.DecimalField(max_digits=10, decimal_places=4)
    pressure = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    temp_min = models.DecimalField(max_digits=10, decimal_places=4)
    temp_max = models.DecimalField(max_digits=10, decimal_places=4)
    main_grnd_level = models.DecimalField(max_digits=10, decimal_places=4)
    main_sea_level = models.DecimalField(max_digits=10, decimal_places=4)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=4)
    wind_deg = models.DecimalField(max_digits=5, decimal_places=2)
    clouds_all = models.CharField(max_length=10)
    rain_3h = models.CharField(max_length=10)
    snow_3h = models.CharField(max_length=10)
    dt = models.DateField()  # time of data measurement
    sys_message = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    sys_sunrise = models.DateField()
    sys_sunset = models.DateField()
    city_id = models.IntegerField()
    name = models.CharField(max_length=50)
    wind_direction = models.CharField(max_length=2)
    duration = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __init__(self, data):
        d = data
        self.coord_lon = str(d['coord']['lon']).replace(',', '.')
        self.coord_lat = str(d['coord']['lat']).replace(',', '.')
        self.lon = coordinate(d['coord']['lon'], 'lon')
        self.lat = coordinate(d['coord']['lat'], 'lat')

        self.weather_main = d['weather'][0]['main']
        self.condition = set_condition(
            d['weather'][0]['id'],
            d['weather'][0]['description'])
        self.weather_icon = d['weather'][0]['icon'] + '.png'

        self.visibility = d.get('visibility', 'нет данных')

        self.main_sea_level = set_pressure(d['main'].get('sea_level'))
        self.main_grnd_level = set_pressure(d['main'].get('grnd_level'))
        self.pressure = set_pressure(d['main'].get('pressure'))
        self.temperature = round(float(d['main'].get('temp')))
        self.temp_min = d['main'].get('temp_min')
        self.temp_max = d['main'].get('temp_max')
        self.humidity = d['main'].get('humidity')

        self.wind_speed = d['wind'].get('speed')
        self.wind_direction = set_wind_direction(d['wind'].get('deg'))

        self.clouds_all = d['clouds'].get('all')
        if d.get('rain') is not None:
            self.rain_3h = d['rain'].get('3h', 'n/a')
        if d.get('snow') is not None:
            self.snow_3h = d['snow'].get('3h', 'n/a')

        self.sys_message = d['sys'].get('message')
        self.sys_sunrise = natural_time(d['sys']['sunrise'])  # восход
        self.dt = natural_time(d['dt'])  # время измерения
        self.sys_sunset = natural_time(d['sys']['sunset'])  # закат
        self.duration = day_duration(d['sys']['sunrise'], d['sys']['sunset'])

        self.city_id = d['id']
        self.name = d['name']
        self.country = d['sys'].get('country')
