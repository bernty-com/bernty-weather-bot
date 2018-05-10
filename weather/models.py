# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.template import Context

import json, requests, datetime

from .model_func import day_duration, set_pressure, set_wind_direction, natural_time, coordinate

conditions = {
200:'гроза с небольшим дождем',
201:'гроза с дождем',
202:'гроза с сильным дождем',
210:'легкая гроза',
211:'гроза',
212:'сильная гроза',
221:'шквальная гроза',
230:'гроза с легкой моросью',
231:'гроза с дождем',
232:'гроза с сильным дождем',
300:'малая изморось',
301:'изморось',
302:'сильный дождь',
310:'легкий дождь, изморось',
311:'дождь, изморось',
312:'сильный дождь, изморось',
313:'ливень и изморось',
314:'сильный ливень и изморось',
321:'ливневый дождь',
500:'легкий дождь',
501:'умеренный дождь',
502:'интенсивный дождь',
503:'очень сильный дождь',
504:'сильный дождь',
511:'ледяной дождь',
520:'легкий ливень',
521:'ливень',
522:'сильный ливень',
531:'шквальный ливневый дождь',
600:'легкий снег',
601:'снег',
602:'снегопад',
611:'дождь со снегом',
612:'дождь',
615:'легкий дождь и снег',
616:'дождь и снег',
620:'легкий душ снег',
621:'снегопад',
622:'сильный снегопад',
701:'туман',
711:'дым',
721:'мгла',
731:'песок, пылевые завихрения',
741:'туман',
751:'песок',
761:'пыль',
762:'вулканический пепел',
771:'шквалы',
781:'торнадо',
800:'чистое небо',
801:'малоблачно',
802:'рассеянные облака',
803:'рваные облака',
804:'облака с просветом',
900:'торнадо',
901:'тропическая буря',
902:'ураган',
903:'холод',
904:'жара',
905:'ветрено',
906:'град',
951:'спокойный',
952:'легкий ветерок',
953:'нежный бриз',
954:'умеренный ветерок',
955:'свежий ветерок',
956:'сильный ветер',
957:'сильный ветер, около шторма',
958:'шторм',
959:'сильный шторм',
960:'буря',
961:'сильный шторм',
962:'ураган'
}

class Country(models.Model):
    # Fields
    brief = models.CharField(max_length=10, primary_key=True, verbose_name='Код страны')
    name = models.CharField(max_length=50, verbose_name='Название')

    #Meta
    class Meta:
        ordering = ["name"]
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    # Python 2.7
    def __unicode__(self):
        return self.name
    
    # Python 3.6
    def __str__(self):
        return self.name

class City(models.Model):
    # Fields
    city_id = models.IntegerField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name='Название')
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, verbose_name='Страна')  
    coord_lon = models.DecimalField(max_digits=19, decimal_places=6, verbose_name='Долгота')
    coord_lat = models.DecimalField(max_digits=19, decimal_places=6, verbose_name='Широта')
    
    #Meta
    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('city.detail', args=[str(self.city_id)])
    
    def get_city_id(self):
        return self.city_id
        
    def __unicode__(self):
        return self.name

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
    main_pressure = models.CharField(max_length=10)
    main_humidity = models.CharField(max_length=10)
    main_temp_min = models.DecimalField(max_digits=10, decimal_places=4)
    main_temp_max = models.DecimalField(max_digits=10, decimal_places=4)
    main_grnd_level = models.DecimalField(max_digits=10, decimal_places=4)
    main_sea_level = models.DecimalField(max_digits=10, decimal_places=4)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=4)
    wind_deg = models.DecimalField(max_digits=5, decimal_places=2)
    clouds_all = models.CharField(max_length=10) # Cloudiness, %
    rain_3h = models.CharField(max_length=10) # 
    snow_3h = models.CharField(max_length=10) # 
    dt  = models.DateField() # time of data measurement
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
        
    def get_forecast(self, id):
        import json, requests
        api_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'id': id,
            'appid': '86400dcb34b136834f8f3eb6a92a59b3',
            'units': 'metric',
            'type': 'accurate',
            'lang': 'ru'
        }
        res = requests.get(api_url, params=params)
        data = None
        if res.status_code == 200:
            data = res.json()
        return data
        
    def set_condition(self,cond):
        return conditions[cond]
            
    def __init__(self, id):
        d = self.get_forecast(id)
        self.coord_lon = d['coord']['lon']
        self.coord_lat = d['coord']['lat']
        self.lon = coordinate(d['coord']['lon'],'lon')
        self.lat = coordinate(d['coord']['lat'],'lat')
        
        self.weather_id = self.set_condition(d['weather'][0]['id'])
        self.weather_main = d['weather'][0]['main']
        self.weather_description = d['weather'][0]['description']
        self.weather_icon = d['weather'][0]['icon'] + '.png'
        
        self.visibility = d.get('visibility','нет данных')
        
        self.main_sea_level = set_pressure(d['main'].get('sea_level'))
        self.main_grnd_level = set_pressure(d['main'].get('grnd_level'))
        self.main_pressure = set_pressure(d['main'].get('pressure'))
        self.temperature = round(float(d['main'].get('temp')))
        self.main_temp_min = d['main'].get('temp_min')
        self.main_temp_max = d['main'].get('temp_max')
        self.main_humidity = d['main'].get('humidity')
        
        self.wind_speed = d['wind'].get('speed')
        self.wind_direction = set_wind_direction(d['wind'].get('deg'))
        
        self.clouds_all = d['clouds'].get('all')
        if d.get('rain') is not None:
            self.rain_3h = d['rain'].get('3h','n/a')
        if d.get('snow') is not None:
            self.snow_3h = d['snow'].get('3h','n/a')
        
        self.sys_message = d['sys'].get('message')
        self.sys_sunrise = natural_time(d['sys']['sunrise']) # восход
        self.dt = natural_time(d['dt']) # время измерения
        self.sys_sunset = natural_time(d['sys']['sunset']) # закат
        self.duration = day_duration(d['sys']['sunrise'], d['sys']['sunset'])
        
        self.city_id = d['id']
        self.name = d['name']
        self.country = d['sys'].get('country')
