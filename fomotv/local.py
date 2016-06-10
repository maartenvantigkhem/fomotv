import sys
from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fomotv',                   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                           # Set to empty string for default.
    },
}


MEDIA_ROOT = 'd:/pwww/fomotv/media/'
#STATIC_ROOT = 'd:/pwww/fomotv/static/'

STATICFILES_DIRS = (
    "d:/pwww/fomotv/static",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

SOCIAL_AUTH_FACEBOOK_KEY = '823460024399342'
SOCIAL_AUTH_FACEBOOK_SECRET = '2884e0dcc2a3f0c64ffeb40ac77862ca'

SOCIAL_AUTH_INSTAGRAM_KEY = 'ddc1042e22f74304be0f847f469942a6'
SOCIAL_AUTH_INSTAGRAM_SECRET = '082e51fb07914c0cb84f5b2f0671036e'


if 'test' in sys.argv or 'testserver' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
    }

MANAGER_EMAIL = "nfokin@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'