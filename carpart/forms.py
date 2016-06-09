# -*- coding: utf-8 -*-

from django import forms
from . import models


class CarPartForm(forms.ModelForm):
    class Meta:
        model = models.CarPart
        fields = ['name', 'producent', 'description', 'price', 'quantity']
