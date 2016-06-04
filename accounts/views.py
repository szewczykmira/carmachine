from django.shortcuts import render
from . import forms


def add_user(request, is_client=False):
    context = {'add_user': True}
    if is_client:
        context['form'] = forms.ClientForm()
    else:
        context['form'] = forms.EmployeeForm()
    return render(request, "accounts/add_user.html", context=context)

