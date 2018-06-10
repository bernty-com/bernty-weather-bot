# -*- coding: utf-8 -*-

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

CITY_PER_PAGE = 20


def index(request):
    context = {}
    # подсчет количества посещений авторизованного пользователя
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context['project_name'] = settings.PROJECT_NAME
    
    # вывод избранных городов (если такие есть) для аворизованого пользователя
    user = request.user
    if user.is_authenticated:
#        logged_user = User.objects.get(username=user)
        content_type_id = ContentType.objects.get(model='city')
        c = ContentType.objects.get_for_model(City)
#        print('KKA1', content_type_id)
        fav_queryset = Favorite.objects.filter(content_type=content_type_id, user__exact=user)
        l = list()
        for f in fav_queryset:
            l.append(f.object_id)
#            print('KKA-2', f.object_id) 
        cities = City.objects.filter(id__in=l)
#        f2 = Favorite.objects.filter(cities__user=user)
#        print('KKA3',f2)
        
        context['object_list'] = cities
                
    return render(
        request,
        'weather/lorem.html',
        context=context,
    )


class CityView(LoginRequiredMixin, ListView):
    template_name = 'weather/city_list.html'
    context_object_name = 'city_lists'
    paginate_by = CITY_PER_PAGE

    def get_queryset(self):
        q = self.request.GET.get('city')
        if q is None:
            # Если пользователь оставил поле поиска пустым
            return City.objects.all()
        else:
            # если запрос содержит точку в конце,
            # то требуется точное соответствие
            # иначе используем все вхождения
            # ищем сначала русское название, если не находим, тогда английское
            if q[-1:] == '.':
                q = q[:-1]
                queryset_local = City.objects.filter(local_name__iexact=q)
                queryset_native = City.objects.filter(name__iexact=q)
            else:
                queryset_local = City.objects.filter(local_name__icontains=q)
                queryset_native = City.objects.filter(name__icontains=q)
            if queryset_local.exists():
                queryset = queryset_local
            else:
                queryset = queryset_native
            return queryset


class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    redirect_field_name = 'next'
    template_name = 'weather/city_detail.html'
    # login_url =  см. настройку LOGIN_URL

    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        forecast = Forecast(pk)
        context['fc'] = forecast
        context['min_max'] = min_max_temperature(
                                    forecast.temp_min,
                                    forecast.temp_max
                                    )
        return context
