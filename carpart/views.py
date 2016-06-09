# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from accounts.models import Account


@login_required(login_url='accounts/login')
def home(request):
    if Account.objects.get_from_user(request.user).is_client():
        return Http404(_("You are not allowed to be here!"))
    context = {
        'parts': models.CarPart.objects.all()
    }
    return render(request, 'carpart/index.html', context)


@login_required(login_url='accounts/login')
def add_part(request, partid=None):
    if Account.objects.get_from_user(request.user).is_client():
        return Http404(_("You are not allowed to be here!"))
    if partid:
        part = models.CarPart.objects.get(id=partid)
        form = forms.CarPartForm(request.POST or None, instance=part)
    else:
        form = forms.CarPartForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if context['form'].is_valid():
            part = context['form'].save()
            messages.success(request, _('Part has been added'))
            return redirect('carpart_home')
        messages.error(request, _("Please review information!"))

    return render(request, 'carpart/add_part.html', context)
