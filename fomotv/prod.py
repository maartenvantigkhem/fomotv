from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fomotv',                   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'fomotv',
        'PASSWORD': 'AZLnHphdxHv9dLd8',
        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                           # Set to empty string for default.
    }
}

MEDIA_ROOT = "/var/www/fomotv.net/fomotv/media/"

STATIC_ROOT = "/var/www/fomotv.net/fomotv/static/"

SOCIAL_AUTH_FACEBOOK_KEY = '637036429766647'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b0356143d3219eb59e0aafa54b87a67b'

SOCIAL_AUTH_INSTAGRAM_KEY = '59367ec6a3b9470eaf6674b2089e3950'
SOCIAL_AUTH_INSTAGRAM_SECRET = 'd3d6f2d73bac4521ae7bfce766b35fd3'

PAYPAL_TEST = False

PAYPAL_WPP_USER = "theroomswebsite_api1.yahoo.com.au"
PAYPAL_WPP_PASSWORD = "CSVENKDMXHWKR4PA"
PAYPAL_WPP_SIGNATURE = "AFcWxV21C7fd0v3bYYYRCpSSRl31A8MB79v-VDcw3wjay.5kpJGaskIf"
PAYPAL_URL = "https://www.paypal.com"

MANAGER_EMAIL = "renatabliss@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MINIFY_JS = True
