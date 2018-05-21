# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.template.context_processors import csrf

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
   
    def get(self, request, *args, **kwargs):
        from django.shortcuts import render_to_response
        from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
        
        context = {}
        context.update(csrf(request))
        
        question = request.GET.get('city')
        if question is not None:
            # если запрос содержит точку в конце, то требуется точное соответствие
            # иначе используем все вхождения
            # ищем сначала русское название, если не находим, тогда английское
            if question[-1:] == '.':
                question = question[:-1] 
                queryset_local = City.objects.filter(local_name__iexact=question)
                queryset_native = City.objects.filter(name__iexact=question)
            else:
                queryset_local = City.objects.filter(local_name__icontains=question)
                queryset_native = City.objects.filter(name__icontains=question)
            if queryset_local.exists():
                searched_city = queryset_local
            else:
                searched_city = queryset_native
            if len(searched_city) > CITY_PER_PAGE:             
                # Paginator start
                # формируем строку URL, которая будет содержать последний запрос
                # Это важно для корректной работы пагинации
                context['needPaginator'] = True
                context['last_city'] = '?city=%s' % question
                current_page = Paginator(searched_city, CITY_PER_PAGE)
                page = request.GET.get('page')
                try:
                    context['city_lists'] = current_page.page(page)
                except PageNotAnInteger:
                    context['city_lists'] = current_page.page(1)
                except EmptyPage:
                    context['city_lists'] = current_page.page(current_page.num_pages)
                #Paginator end
            else:
                context['needPaginator'] = False
                context['city_lists'] = searched_city           
        return render_to_response(template_name=self.template_name, context=context)

class CityDetail(DetailView):
    queryset = City.objects.all()
    template_name = 'weather/city_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None) 
        context['fc'] = Forecast(pk)
        return context

