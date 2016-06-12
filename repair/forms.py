# -*- coding: utf-8 -*-

from django import forms
from . import models


class RepairForm(forms.ModelForm):
    class Meta:
        model = models.Repair
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        self.fields['order_date'].help_text = 'YYYY-MM-DD'
        self.fields['receipt_date'].help_text = 'YYYY-MM-DD'