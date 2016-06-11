# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from .helpers import generate_row
from accounts.models import Account
import json
from CarMachine.helper_models import delete_view


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
    return delete_view(request, models.CarPart)


@login_required(login_url='accounts/login')
def get_parts(request):
    if Account.objects.get_from_user(request.user).is_client() or\
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    search_val = request.GET['input']
    objects = models.CarPart.objects.filter(
        Q(name__icontains=search_val) | Q(producent__icontains=search_val))
    if bool(request.GET['sort']):
        objects = objects.order_by(request.GET['sort'])
    row_list = []
    i = 1
    for elem in objects:
        row_list.append(generate_row(elem, i))
        i += 1
    context = {
        'objects': row_list,
    }
    return HttpResponse(json.dumps(context), content_type='application/json')
