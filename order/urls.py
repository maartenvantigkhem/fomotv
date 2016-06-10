from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^paypal/start$', views.paypal_start, name='paypal_start'),
    url(r'^paypal/confirm$', views.paypal_confirm, name='paypal_confirm'),
    url(r'^paypal/end$', views.paypal_end, name='paypal_end'),
    url(r'^save$', views.save, name='save')
)