# -*- coding: utf-8 -*-
from django.conf.urls import url
 
from django.contrib.auth.views import LogoutView
from . import views
 
app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.ELoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.ESignUpView.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]