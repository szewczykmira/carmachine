# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from accounts.models import Account
import json


@login_required(login_url='accounts/login')
def home(request):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))
    context = {
        'parts': models.CarPart.objects.all()
    }
    return render(request, 'carpart/index.html', context)


@login_required(login_url='accounts/login')
def add_part(request, partid=None):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
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


@login_required(login_url='accounts/login')
def delete_part(request):
    if Account.objects.get_from_user(request.user).is_client() or\
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    if request.method == 'POST' and request.is_ajax():
        try:
            object = models.CarPart.objects.get(id=request.POST['object_id'])
            object.delete()
            success = True
        except models.CarPart.DoesNotExist:
            success = False
        return HttpResponse(json.dumps({'success': success}),
                            content_type='application/json')
