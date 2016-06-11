# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="provider_home"),
    url(r'^add/$', views.add_provider, name="provider_add"),
    url(r'edit/(?P<provider>\d+)/$', views.add_provider, name="provider_edit"),
    url(r'delete/$', views.delete_provider, name="provider_delete"),
    url(r'search/$', views.get_providers, name="provider_search"),
]