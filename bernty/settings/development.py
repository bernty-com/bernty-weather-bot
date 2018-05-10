# -*- coding: utf-8 -*-

from bernty.settings.common import *

DEBUG = bool(os.environ.get('DJANGO_DEBUG', True) )
ALLOWED_HOSTS = ['localhost','127.0.0.1']

SECRET_KEY = os.environ.get('SECRET_KEY','wft317e_vktxe+s-s!t+@_=)f%f$utmr)9dquocaht#^6(-x^d')

#POSTGRES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "KKA",
        "USER": "KKA",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
