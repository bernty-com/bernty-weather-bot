# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import ELoginView  # Представление для авторизации из модуля accounts

urlpatterns = [
    url(r'^admin/login/', ELoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^fav/', include('fav.urls')),
    url(r'^telegrambot/', include('telegrambot.urls', namespace='telegrambot')),
    url(r'^', include('weather.urls')),
]
