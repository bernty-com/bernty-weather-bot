# -*- coding: utf-8 -*-

"""
WSGI config for bernty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

#путь к проекту
sys.path.insert(0, '/home/b/berntyru/public_html')

#путь к фреймворку
sys.path.insert(0, '/home/b/berntyru/public_html/bernty')

#путь к виртуальному окружению
sys.path.insert(0, '/home/b/berntyru/env/lib64/python2.7/site-packages/')

from django.core.wsgi import get_wsgi_application

#os.environ["DJANGO_SETTINGS_MODULE"] = "bernty.settings.production"
os.environ["DJANGO_SETTINGS_MODULE"] = "bernty.settings"

application = get_wsgi_application()

from django.contrib.auth.handlers.modwsgi import check_password

