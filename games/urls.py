from django.conf.urls import url
from django.contrib import admin

import games.views


urlpatterns = [
    url(r'^list/$', games.views.list_view, name='list'),
    url(r'^delete/(?P<pk>\d+)$', games.views.delete, name='delete'),
]