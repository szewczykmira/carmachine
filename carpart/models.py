# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

class CarPart(models.Model):
    name = models.CharField(
            verbose_name=_("Name"),
            max_length=100)
    producent = models.CharField(
            verbose_name=_("Producent"),
            max_length=100)
    description = models.TextField(
            verbose_name=_("Description"))
    price = models.FloatField(
            verbose_name=_("Price"))
    quantity = models.PositiveIntegerField(
            verbose_name=_("Quantity"))
