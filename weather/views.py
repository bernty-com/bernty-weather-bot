# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import City, Country, Forecast
#from .forms import CityForm

class CityView(ListView):
    template_name = 'weather/city_list.html'
    context_object_name = 'city_lists'
   
    def get(self, request, *args, **kwargs):
        from django.shortcuts import render_to_response
        from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
        
        context = {}
        
        question = request.GET.get('city')
        if question is not None:
            searched_city = City.objects.filter(name__icontains=question)
            print(searched_city)
            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_city'] = '?city=%s' % question

            current_page = Paginator(searched_city, 20)
            page = request.GET.get('page')
            try:
                context['city_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['city_lists'] = current_page.page(1)
            except EmptyPage:
                context['city_lists'] = current_page.page(current_page.num_pages)
        return render_to_response(template_name=self.template_name, context=context)

class CityDetail(DetailView):
    queryset = City.objects.all()
    template_name = 'weather/city_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None) 
        context['weather'] = Forecast(pk)
        return context

