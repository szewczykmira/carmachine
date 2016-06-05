# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^client/add/$', views.add_user, {'is_client': True}, name="add_client"),
    url(r'employee/add/$', views.add_user, name="add_employee"),
    url(r'login/$', views.login_user, name="login"),
    url(r'logout/$', views.logout_user, name="logout"),
]