# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import Client, Employee
from carpart.models import CarPart


class Repair(models.Model):
    client = models.ForeignKey(
            Client, 
            verbose_name=_("Client"))
    employee = models.ForeignKey(
            Employee,
            verbose_name=_("Employee"))
    order_date = models.DateField(
            verbose_name=_("Order date"))
    receipt_date = models.DateField(
            verbose_name=_("Receipt date"),
            blank=True, null=True)
    price = models.FloatField(
            verbose_name=_("Price"))
    description = models.TextField(
            verbose_name=_("Description"), 
            blank=True, null=True)


class RepairItem(models.Model):
    carpart = models.ForeignKey(
            CarPart,
            verbose_name=_("Car Part"))
    repair = models.ForeignKey(
            Repair, 
            verbose_name=_("Repair"))
    price = models.FloatField(
            verbose_name=_("Car part's price"))
