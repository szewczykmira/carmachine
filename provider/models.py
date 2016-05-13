# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

class Provider(models.Model):
    name = models.CharField(
            verbose_name=_("Name"),
            max_length=100)
    address = models.TextField(
            verbose_name=_("Address"))
    telephone = models.CharField(
            verbose_name=_("Telephone"),
            max_length=9)
    e-mail = models.EmailField(
            verbose_name=_("E-mail address"))
    description = models.TextField(
            verbose_name=_("Descritpion"))
    # TODO Add nip/regon validator
    nip = models.CharField(
            verbose_name=_("NIP"),
            null=True, blank=True)
    regon = models.CharField(
            verbose_name=_("REGON"),
            null=True, blank=True)


