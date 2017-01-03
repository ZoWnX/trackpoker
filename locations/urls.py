from django.conf.urls import url
from django.contrib import admin

import locations.views


urlpatterns = [
   url(r'^list/$', locations.views.locations_list_view, name='list'),
   url(r'^delete/(?P<pk>\d+)$', locations.views.delete, name='delete'),
]