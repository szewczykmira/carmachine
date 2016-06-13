# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from provider.models import Provider
from carpart.models import CarPart


class Order(models.Model):
    provider = models.ForeignKey(
            Provider,
            verbose_name=_("Provider"))
    price = models.FloatField(
            verbose_name=_("Price"), default=0)
    order_date = models.DateField(
            verbose_name=_("Order date"), 
            blank=True, null=True)
    receipt_date = models.DateField(
            verbose_name=_("Date of receipt"),
            blank=True, null=True)

    def already_ordered(self):
        return True if self.order_date is not None else False

    def get_items(self):
        return OrderItem.objects.filter(order=self)

    def calculate(self):
        self.price = reduce(lambda x, y: y.price+x, list(self.get_items()), 0)
        self.save()


class OrderItem(models.Model):
    cart_part = models.ForeignKey(
            CarPart, 
            verbose_name=_("Cart part"))
    order = models.ForeignKey(
            Order,
            verbose_name=_("Order"))
    price = models.FloatField(
            verbose_name=_("Price"))
