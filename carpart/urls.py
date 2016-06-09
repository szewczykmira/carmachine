# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="carpart_home"),
    url(r'add/$', views.add_part, name="carpart_add"),
]