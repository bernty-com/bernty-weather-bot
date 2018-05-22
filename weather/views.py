# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import City, Country, Forecast

CITY_PER_PAGE = 20

def index(request):
    context = {}
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'weather/lorem.html',
        context=context,
    )
    
class CityView(ListView):
    template_name = 'weather/city_list.html'
    context_object_name = 'city_lists'
    paginate_by = CITY_PER_PAGE
   
    def get_queryset(self):
        q = self.request.GET.get('city')

        if q is not None:
            # если запрос содержит точку в конце, то требуется точное соответствие
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
                return queryset_local
            else:
                return queryset_native
        else:
            return City.objects.all()

class CityDetail(LoginRequiredMixin, DetailView):
#    login_url =  см. настройку LOGIN_URL
    redirect_field_name = 'next'
    queryset = City.objects.all()
    template_name = 'weather/city_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None) 
        context['fc'] = Forecast(pk)
        return context

