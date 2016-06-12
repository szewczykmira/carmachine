# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="order_home"),
    url(r'add/$', views.add_order, name="order_add"),
    url(r'edit/(?P<order_id>\d+)/$', views.add_order, name="order_edit"),
]