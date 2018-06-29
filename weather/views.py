# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.template.context_processors import csrf
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from django.core.urlresolvers import reverse

from .models import City, Forecast
from fav.models import Favorite

from .model_func import min_max_temperature

from django.contrib.contenttypes.models import ContentType

from pyowm import OWM

from django_pyowm.models import Weather as djWeather
from django_pyowm.models import Location as djLocation
from django_pyowm.models import Observation as djObservation

CITY_PER_PAGE = 20


def set_common_context_vars(request):
    context = {}
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context['num_visits'] = request.session['num_visits']
    context['is_first_time'] = True if context['num_visits'] == 1 else False  
    context['project_name'] = settings.PROJECT_NAME
    return context

def index(request):
    context = {}
    # вывод избранных городов (если такие есть) для авторизованого пользователя
    user = request.user
    if user.is_authenticated:
        content_type_id = ContentType.objects.get(model='city')
        fav_queryset = Favorite.objects.filter(content_type=content_type_id, user__exact=user)
        l = list()
        for f in fav_queryset:
            l.append(f.object_id)
        cities = City.objects.filter(id__in=l)
        
        context['object_list'] = cities
                
    common_context = set_common_context_vars(request)
    context.update(common_context)
    return render(
        request,
        'weather/lorem.html',
        context=context,
    )


class CityView(LoginRequiredMixin, ListView):
    model = djLocation
    template_name = 'weather/city_list.html'
    context_object_name = 'object_list'
    paginate_by = CITY_PER_PAGE  # кол-во элементов на страницу

    def get_queryset(self):
        q_country = self.request.GET.get('country')
        if len(q_country) == 0:
            q_country = None 
        q = self.request.GET.get('city')
        if len(q) == 0:
            return None
        else:
            # если запрос содержит точку в конце,
            # то требуется точное соответствие
            # иначе используем все вхождения
            # ищем сначала русское название, если не находим, тогда английское
            if q[-1:] == '.':
                q = q[:-1]
                matching = 'nocase'
                queryset = City.objects.filter(name__iexact=q)
            else:
                matching = 'like'
                queryset = City.objects.filter(name__icontains=q)

            locations = self.pyowm_get_city(q, q_country, matching)
        return queryset

    def get_queryset_new(self):
        q_country = self.request.GET.get('country')
        if len(q_country) == 0:
            q_country = None 
        q_city = self.request.GET.get('city')
        if len(q_city) == 0:
            return None
        else:
            # если запрос содержит точку в конце,
            # то требуется точное соответствие
            # иначе используем все вхождения
            if q_city[-1:] == '.':
                q_city = q_city[:-1]
                matching = 'nocase'
            else:
                matching = 'like'
            locations = self.pyowm_get_city(q_city, q_country, matching)
            return locations

    def pyowm_get_city(self, city, country, matching='nocase'):
        owm = OWM(API_key=settings.OWM_KEY, language='ru')
        # функция обращается к локальному хранилищу городов в zip-файле
        reg = owm.city_id_registry()
        city_list = reg.locations_for(city_name=city, country=country, matching=matching)
        
        # и сохраняет в БД результаты поиска
        for c in city_list:
            l = djLocation.from_entity(c)
            if not djLocation.objects.filter(city_id=l.city_id).exists():
                l.save()
                print('KKA START', l.city_id, l.name, 'saved')
            else:
                print('KKA START', l.city_id, l.name, 'NOT saved')
        return city_list


class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    redirect_field_name = 'next'
    template_name = 'weather/city_detail.html'
    # login_url =  см. настройку LOGIN_URL

# сессионные куки работают, но не закрыт вопрос с их устареванием и удалением
    def get_forecast(self, id):
        wdata = 'weatherdata' + str(id)
        is_cached = (wdata in self.request.session)
        
        if not is_cached:
            api_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'id': id,
                'type': 'accurate',
                'lang': 'ru',
                'units': 'metric',
                'appid': settings.OWM_KEY,
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                self.request.session[wdata] = response.json()

        return self.request.session[wdata]

    def pyowm_get_weather(self, id):
        owm = OWM(API_key=settings.OWM_KEY,language='ru')
        if owm.is_API_online():
            observation = owm.weather_at_id(id) 
            weather = observation.get_weather()
            location = observation.get_location()
            w = Weather.from_entity(weather).save()
#  огрубляет данные координат до 2 знаков после запятой почему-то
#            l = Location.from_entity(location).save()
            o = djObservation.from_entity(observation).save()

        return weather

    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        weatherdata = self.get_forecast(pk)
        pyowmdata = self.pyowm_get_weather(int(pk))
        forecast = Forecast(weatherdata)
        context['fc'] = forecast
        context['min_max'] = min_max_temperature(
                                    forecast.temp_min,
                                    forecast.temp_max
                                    )
        context['google_api_key'] = settings.GOOGLE_API_KEY
        common_context = set_common_context_vars(self.request)
        context.update(common_context)
        return context
        
class StationDetailView(LoginRequiredMixin, DetailView):
    pass