# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from . import managers


class Account(User):
    objects = managers.AccountManager()

    class Meta:
        proxy = True

    def is_employee(self):
        try:
            emp = self.employee
            return True
        except:
            return False

    def is_client(self):
        try:
            cli = self.client
            return True
        except:
            return False
    

class Employee(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    contract_begin = models.DateField(
        verbose_name=_("Begin of contract"))
    telephone = models.CharField(
        verbose_name=_("Telephone"), max_length=9)
    address = models.TextField(
        verbose_name=_("Address"))
    salary = models.FloatField(
        verbose_name=_("Salary"),
        default=0)

    def __unicode__(self):
        return unicode(self.account)


class Client(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(
        verbose_name=_("Telephone"), max_length=9)
    address = models.TextField(
        verbose_name=_("Address"))

    def __unicode__(self):
        return unicode(self.account)
