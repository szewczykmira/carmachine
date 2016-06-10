# -*- coding: utf-8 -*-

from django import forms
from . import models


class ProviderForm(forms.ModelForm):
    class Meta:
        model = models.Provider
        fields = '__all__'