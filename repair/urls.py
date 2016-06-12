# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="repair_home"),
    url(r'^clients/$', views.home, kwargs={'clients': True},  name="repair_home_client"),
    url(r'add/$', views.add_repair, name="repair_add"),
    url(r'edit/(?P<repair_id>\d+)/$', views.add_repair, name="repair_edit"),
    #url(r'(?P<order_id>\d+)/$', views.display_order, name="order_display"),
    #url(r'(?P<order_id>\d+)/delete/$', views.delete_order, name="order_disp_delete"),
    #url(r'item/add/(?P<order_id>\d+)/$', views.add_item, name="order_item_add"),
    #url(r'delete/$', views.delete_order, name="order_delete"),
    #url(r'search/$', views.get_orders, name="order_get"),
]