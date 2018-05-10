# -*- coding: utf-8 -*-

# https://thinkster.io/tutorials/configuring-django-settings-for-production
from bernty.settings.common import *

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True) )
ALLOWED_HOSTS = ['bernty.ru']

SECRET_KEY = os.environ.get('SECRET_KEY','wft317e_vktxe+s-s!t+@_=)f%f$utmr)9dquocaht#^6(-x^d')

#POSTGRES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "berntyru",
        "USER": "berntyru",
        "PASSWORD": "WUbuAT2xHd",
        "HOST": "pg.sweb.ru",
        "PORT": "5432",
        "OPTIONS": {
            "client_encoding": "UTF8"
        },
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
