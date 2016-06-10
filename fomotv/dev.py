from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'xgb_fomotv',                   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'xgb_fomotv',
        'PASSWORD': '7c3c479dcgh',
        'HOST': 'postgres55.1gb.ru',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                           # Set to empty string for default.
    }
}

MEDIA_ROOT = '/home/albedo/django/fomotv/media/'

STATIC_ROOT = "/home/albedo/django/fomotv/static/"

SOCIAL_AUTH_FACEBOOK_KEY = '823459407732737'
SOCIAL_AUTH_FACEBOOK_SECRET = '9d1d3a649bc2aae5d4ae93d8a4d9b59d'

SOCIAL_AUTH_INSTAGRAM_KEY = 'eeb10b8af2694d46bcb3f764ae6602f7'
SOCIAL_AUTH_INSTAGRAM_SECRET = 'adb7f2b95b744e8f8471e412eab88ed5'

