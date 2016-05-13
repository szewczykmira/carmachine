# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Account(User):
    class Meta:
        proxy = True
    

class Employee(Account):
   contract_begin = models.DateField(
           verbose_name=_("Begin of contract"))
   telephone = models.CharField(
           verbose_name=_("Telephone"), max_length=9)
   address = models.TextField(
           verbose_name=_("Address"))
   salary = models.FloatField(
           verbose_name=_("Salary"))

class Client(Account):
    telephone = models.CharField(
            verbose_name=_("Telephone"), max_length=9)
    address = models.TextField(
            verbose_name=_("Address"))
