# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from . import models


class ClientForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label=_("Confirm password"),
        widget=forms.PasswordInput())

    class Meta:
        model = models.Client
        fields = ['password', 'username', 'first_name', 'last_name',
                  'email', 'telephone', 'address']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.order_fields(['username', 'first_name', 'last_name', 'email',
                           'password', 'confirm_password', 'telephone',
                           'address'])

    def clean_confirm_password(self):
        pswd2 = self.cleaned_data.get('confirm_password')
        if not self.cleaned_data.get('password') == pswd2:
            raise forms.ValidationError(_("Passwords doesn't match!"))
        return pswd2


class EmployeeForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label=_("Confirm password"),
        widget=forms.PasswordInput())

    class Meta:
        model = models.Employee
        fields = ['password', 'username', 'first_name', 'last_name',
                  'email', 'telephone', 'address', 'contract_begin']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['contract_begin'].widget = forms.DateInput(
            attrs={'class': 'form-control'})
        self.order_fields(['username', 'first_name', 'last_name', 'email',
                           'password', 'confirm_password', 'telephone',
                           'address', 'contract_begin'])

    def clean_confirm_password(self):
        pswd2 = self.cleaned_data.get('confirm_password')
        if not self.cleaned_data.get('password') == pswd2:
            raise forms.ValidationError(_("Passwords doesn't match!"))
        return pswd2
