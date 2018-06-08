# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^city/(?P<pk>[0-9]+)/$', views.CityDetailView.as_view(), name='city.detail'),
    url(r'^citylist/$', views.CityView.as_view(), name='city_list'),
    url(r'^$', views.index, name='index'),
]