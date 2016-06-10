from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fomotv_dev',                   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'fomotv',
        'PASSWORD': 'AZLnHphdxHv9dLd8',
        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                           # Set to empty string for default.
    }
}

MEDIA_ROOT = "/var/www/uwsgi/fomotv/media/"

STATIC_ROOT = "/var/www/uwsgi/fomotv/static/"

SOCIAL_AUTH_FACEBOOK_KEY = '823459407732737'
SOCIAL_AUTH_FACEBOOK_SECRET = '9d1d3a649bc2aae5d4ae93d8a4d9b59d'

SOCIAL_AUTH_INSTAGRAM_KEY = 'eeb10b8af2694d46bcb3f764ae6602f7'
SOCIAL_AUTH_INSTAGRAM_SECRET = 'adb7f2b95b744e8f8471e412eab88ed5'

#SOCIAL_AUTH_FACEBOOK_KEY = '823459407732737'
#SOCIAL_AUTH_FACEBOOK_SECRET = '9d1d3a649bc2aae5d4ae93d8a4d9b59d'

#SOCIAL_AUTH_INSTAGRAM_KEY = '5243ad4485714b97b1348ecb3828e3e6'
#SOCIAL_AUTH_INSTAGRAM_SECRET = 'a0b270bdcc11498c8ec6b0a79b6e6643'

MANAGER_EMAIL = "nfokin@gmail.com"