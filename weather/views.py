# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


from .models import City, Forecast, FavoriteCity


CITY_PER_PAGE = 20


def index(request):
    context = {}
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context['project_name'] = settings.PROJECT_NAME
    
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
#    queryset = City.objects.all()
    template_name = 'weather/city_detail.html'
    # login_url =  см. настройку LOGIN_URL

    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
#        city = City.objects.get(pk=pk)
# не решено. Надо взять настоящего пользователя
        user = 2 # User.objects.all() #  auth.get_user(request)
        context['fc'] = Forecast(pk)
        context['is_favorited'] = FavoriteCity.objects.filter(
            city__exact=pk,
            user__exact=user
            ).exists()
        return context

    def switch_favorite(request, pk, *args, **kwargs):
        city = City.objects.get(pk=pk)
        user = 2 #  User.objects.all()
        favorite = FavoriteCity.objects.filter(city__exact=pk, user__exact=user)
        if favorite.exists():
            count_deleted = favorite.delete() 
        else: 
            FavoriteCity.objects.create(city=city, user=user)
        self.get_context_data(**kwargs)

    

class FavoriteCityView(View):
    context_object_name = 'city'
#    context_object_name = 'favorite-city-view'
#    template_name = 'weather/city_detail.html'
#    User = get_user_model()

    def get(self, request, *args, **kwargs):
        user = auth.get_user(request)
#        pk = kwargs['pk']
        print('KKA START GET', user, 'KKA END')
        context = {}
        context.update(csrf(request))
        if request.user.is_authenticated:
            user = get_object_or_404(User, username=request.user.username)
            print('KKA START GET', user.is_authenticated, 'KKA END')
#           context['extra'] = 'extra'
        else:
            pass
        return render_to_response(template_name='weather/city_detail.html', context=context)

    def post(self, request, *args):
#        print(kwargs)
        user = request.user
        print('KKA START POST',user,'KKA END')
        pk = self.args[0]
#        pk=int(kwargs['pk'])
#        city = get_object_or_404(City, pk=pk)
#        favorite = FavoriteCity.objects.filter(city__exact=pk, user__exact=user)
#        if favorite.exists():
#            count_deleted = favorite.delete() 
#        else: 
#            response = FavoriteCity.objects.create(city=city, user=user)
        return super(FavoriteCityView, self).post(request)

    def get_redirect_url(self, *args, **kwargs):
        pass

# не решено. НАдо делать через class View
def make_favorite_city(request, pk):
    city = City.objects.get(pk=pk)
    user = request.user
    favorite = FavoriteCity.objects.filter(city__exact=pk, user__exact=user)
    if favorite.exists():
        count_deleted = favorite.delete()
    else:
        response = FavoriteCity.objects.create(city=city, user=user)
    return render('city.detail')
