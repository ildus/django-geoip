# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django_geoip.views import set_location

urlpatterns = patterns('',
    url(r'^setlocation/', set_location, name='geoip_change_location'),
)
