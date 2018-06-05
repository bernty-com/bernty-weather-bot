# -*- coding: utf-8 -*-
"""
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import environ # pip install django-environ

# /Users/KKA/Dropbox/Site/2018.bernty.ru
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
APPS_DIR = ROOT_DIR.path('public_html')
ENV_DIR = str(APPS_DIR('bernty'))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = '/home/b/berntyru/public_html/media'
MEDIA_ROOT = str(APPS_DIR('media'))

PROJECT_NAME = 'The Bernty Project'
# Указываем тип переменных и значение по умолчанию, если переменная не инициализирована в .env-файле.  

env = environ.Env(
    SECRET_KEY=str,
    DEBUG=(bool, True),
    DATABASE_URL=str,
    ALLOWED_HOSTS = (list,['bernty.ru']),
    KKA_TEST=(str,'No test'),
)

environ.Env.read_env() # reading .env file

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')
#os.environ.get('SECRET_KEY','my-secret-key-here')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')
if DEBUG:
    ALLOWED_HOSTS += ['localhost','127.0.0.1','testserver']

ADMINS = env('ADMINS')

# Telegram Bot setting
TELEGRAM_BOT_HANDLERS_CONF = "berntybot.bot_handlers"
TELEGRAM_BOT_TOKEN_EXPIRATION = "2" # tow hours before a token expires
SITE_ID=1 # bernty.ru
KKA_TEST = env('KKA_TEST')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': str(APPS_DIR)  + '/log/debug.log',
# '/Users/KKA/Dropbox/Site/2018.bernty.ru/public_html/log/debug.log',
        },
    },     
    'loggers': {
        'telegrambot': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }   
}


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'bootstrap3', # design
    'accounts.apps.AccountsConfig',
    'telegrambot',
    'rest_framework',
]
LOCAL_APPS = [
    'weather', 
    'berntybot',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'bernty.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bernty.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#POSTGRES
DATABASES = {
    'default': env.db('DATABASE_URL'), 
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    #'remote': env.db('REMOTE_URL')
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=False)
DATABASES['default'].update(db_from_env)

test = {'TEST':{'NAME':'test_KKA'}}
#DATABASES['default'].update(test)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LOGIN_URL = '/accounts/login/'
#LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.spaceweb.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'robot@bernty.ru'
EMAIL_HOST_PASSWORD = 'UXW8ayjLXt' # env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MAILER_EMAIL_BACKEND = EMAIL_BACKEND