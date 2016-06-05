from django.shortcuts import render
from . import forms


def add_user(request, is_client=False):
    context = {'add_user': True}
    if is_client:
        context['form'] = forms.ClientForm(request.POST or None)
    else:
        context['form'] = forms.EmployeeForm(request.POST or None)
    if request.POST:
        if context['form'].is_valid():
            #user = context['form'].save()
            print "Udalo sie"
    return render(request, "accounts/add_user.html", context=context)

