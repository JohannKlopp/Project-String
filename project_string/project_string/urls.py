from django.conf.urls import patterns, include, url
from django.contrib import admin
from pstring import views

urlpatterns = patterns('',
    url(r'^$', include('pstring.urls')),
    url(r'^(?P<short>[-bcdfghjkmnpqrstvwxyzBCDFGHJKMNPQRSTVWXY3456789]+)/$', views.resolve_landing, name='resolve_landing'),
    url(r'^generate/$', views.show_form, name='generate'),                   
)
