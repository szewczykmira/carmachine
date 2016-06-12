# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import password_change
from . import views

urlpatterns = [
    url(r'^client/add/$', views.add_user, {'is_client': True}, name="add_client"),
    url(r'^employee/add/$', views.add_user, name="add_employee"),
    url(r'^login$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^panel/$', views.panel, name="accounts_panel"),
    url(r'^panel/client/$', views.client_panel, name='client_panel'),
    url(r'^panel/employee/$', views.employee_panel, name='employee_panel'),
    url(r'^panel/admin/$', views.admin_panel, name='admin_panel'),
    url(r'^activate/$', views.toggle_activate_user, name='toggle_activate_user'),
    url(r'^salary/change/$', views.change_salary, name='change_salary'),
    url(r'^employee/delete/$', views.delete_user, {'employee': True}, name="delete_employee"),
    url(r'^client/delete/$', views.delete_user, name="delete_client"),
    url(r'^employee/all/$', views.display_users, {'employee': True}, name='display_employees'),
    url(r'^client/all/$', views.display_users, name='display_clients'),
    url(r'^password/change/$', password_change,
        {'template_name': 'accounts/password_change.html',
         'post_change_redirect': '/accounts/panel/'}, name='password_change'),
    url(r'^update/$', views.update_account, name='update_account'),
]