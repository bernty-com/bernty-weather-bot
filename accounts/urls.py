# -*- coding: utf-8 -*-
from django.conf.urls import url
 
from django.contrib.auth.views import LogoutView
from . import views
 
app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.ELoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]