# -*- coding: utf-8 -*-

from django import forms
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'
        fields = ['provider', 'order_date', 'receipt_date']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['order_date'].help_text = 'YYYY-MM-DD'
        self.fields['receipt_date'].help_text = 'YYYY-MM-DD'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = models.OrderItem
        fields = ['cart_part', 'price']