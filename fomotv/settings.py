"""
Django settings for fomotv project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't4dmr^s=l=-^n58^8)xiqnb3m)9ya6f7(7t7s6(zi(1ups2kyh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'select_multiple_field',
    'rest_framework',
    'main',
    'order',
    'social.apps.django_app.default',
    #'paypal.standard.ipn',
    'paypal.standard',
    'paypal.pro',
    'treebeard',
    'questionnaire',
    'mailchimp'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.instagram.InstagramOAuth2',
)

ROOT_URLCONF = 'fomotv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\', '/'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

WSGI_APPLICATION = 'fomotv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

#This is what defines which model to be picked up as the User Model
#If this is not defined, then the default model defined by Django is picked up.
AUTH_USER_MODEL = 'main.MyUser'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'main.pipeline.save_profile',
    'main.pipeline.add_user_to_mailchimp',
    'social.pipeline.user.user_details'
 
)

REST_FRAMEWORK = {
 #   'DEFAULT_PERMISSION_CLASSES': [
 #       'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
 #   ],
    #'DEFAULT_AUTHENTICATION_CLASSES': (
    #    'restapi.auth.BasicUserAuthentication',
    #),
    'PAGINATE_BY': None,
    'PAGINATE_BY_PARAM': 'page_size',
}

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

#The permissions that you are asking Facebook to provide you
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_photos', ]

#The actual data being queried from facebook (in addition to username). If for example email is not added, then email won't be sent.
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}

#PayPal settings
PAYPAL_RECEIVER_EMAIL = "yourpaypalemail@example.com"

#Enable this for Sandbox Paypal Testing
PAYPAL_TEST = True
PAYPAL_WPP_USER = "sdk-three_api1.sdk.com"
PAYPAL_WPP_PASSWORD = "QFZCWN5HZM8VBG7Q"
PAYPAL_WPP_SIGNATURE = "A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU"
PAYPAL_URL = "https://www.sandbox.paypal.com"


#Enable this for Live Paypal Testing.
#PAYPAL_TEST = False
#PAYPAL_WPP_USER = "theroomswebsite_api1.yahoo.com.au"
#PAYPAL_WPP_PASSWORD = "CSVENKDMXHWKR4PA"
#PAYPAL_WPP_SIGNATURE = "AFcWxV21C7fd0v3bYYYRCpSSRl31A8MB79v-VDcw3wjay.5kpJGaskIf"
#PAYPAL_URL = "https://www.paypal.com/nvp"

DEFAULT_USER_AVATAR = '/static/img/default-user-avatar.jpg'
MANAGER_EMAIL = "vikram@f2pictures.com"

MINIFY_JS = False
