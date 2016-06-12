# -*- coding: utf-8 -*-

from django import forms
from . import models


class RepairForm(forms.ModelForm):
    class Meta:
        model = models.Repair
        fields = '__all__'