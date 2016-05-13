# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from .models_helper import validate_nip, validate_regon


class Provider(models.Model):
    name = models.CharField(
            verbose_name=_("Name"),
            max_length=100)
    address = models.TextField(
            verbose_name=_("Address"))
    telephone = models.CharField(
            verbose_name=_("Telephone"),
            max_length=9)
    email = models.EmailField(
            verbose_name=_("E-mail address"))
    description = models.TextField(
            verbose_name=_("Descritpion"))
    nip = models.CharField(
            verbose_name=_("NIP"),
            max_length=10,
            null=True, blank=True,
            validators=[validate_nip])
    regon = models.CharField(
            max_length=9,
            verbose_name=_("REGON"),
            null=True, blank=True,
            validators=[validate_regon])


