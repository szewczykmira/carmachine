# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="carpart_home"),
    url(r'^add/$', views.add_part, name="carpart_add"),
    url(r'^edit/(?P<partid>\d+)/$', views.add_part, name="carpart_edit"),
    url(r'^delete/$', views.delete_part, name='delete_part'),
    url(r'^search/$', views.get_parts, name='get_parts'),
]
