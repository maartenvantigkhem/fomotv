import sys
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'simple_test_db'
    }
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

MANAGER_EMAIL = "nfokin@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)