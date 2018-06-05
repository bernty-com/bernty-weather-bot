# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
#    url(r'^city/(?P<pk>[0-9]+)/favorite/$', views.CityDetailView.switch_favorite, name='favorite-city-func'),
    url(r'^city/(?P<pk>[0-9]+)/favorite/$', views.make_favorite_city, name='favorite-city-func'),
    url(r'^city/(?P<pk>[0-9]+)/$', views.CityDetailView.as_view(), name='city.detail'),
    url(r'^city/(?P<pk>[0-9]+)/fav/$', views.FavoriteCityView.as_view(), name='favorite-city-view'),
    url(r'^citylist/$', views.CityView.as_view(), name='city_list'),
    url(r'^$', views.index, name='index'),
]