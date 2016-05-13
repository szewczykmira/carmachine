# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from cartpart.models import CartPart
from provider.models import Provider

class OrderItem(models.model):
    cart_part = models.ForeignKey(
            CartPart, 
            verbose_name=_("Cart part"))
    order = models.ForeignKey(
            Order,
            verbose_name=_("Order"))
    price = models.FloatField(
            verbose_name=_("Price"))

class Order(models.Model):
    provider = models.ForeignKey(
            Provider,
            verbose_name=_("Provider"))
    price = models.FloatField(
            verbose_name=_("Price"))
    order_date = models.DateField(
            verbose_name=_("Order date"), 
            blank=true, null=true)
    receipt_date = models.DateField(
            verbose_name=_("Date of receipt"),
            blank=true, null=true)

    def already_ordered(self):
        return True if self.order_date is not null else False
