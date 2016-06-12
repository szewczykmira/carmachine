# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
#from .helpers import generate_row_order, generate_row_item
from accounts.models import Account
from CarMachine.helper_views import home_view, delete_view
import json


@login_required(login_url='/accounts/login')
def home(request, clients=False):
    if clients:
        context = {'objects': models.Repair.objects.filter(
            client=request.user.client)}
        return render(request, 'repair/index.html', context)
    else:
        return home_view(request, models.Repair, 'repair/index.html')


@login_required(login_url='/accounts/login')
def add_repair(request, repair_id=None):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))

    if repair_id:
        repair = get_object_or_404(models.Repair, id=repair_id)
        form = forms.RepairForm(request.POST or None, instance=repair)
    else:
        form = forms.RepairForm(request.POST or None)

    context = {'form': form}
    if request.method == 'POST':
        if context['form'].is_valid():
            repair = context['form'].save()
            messages.success(request, _('Repair has been added'))
            return redirect('repair_home')
        messages.error(request, _("Please review information!"))

    return render(request, 'repair/add_repair.html', context)


@login_required(login_url='/accounts/login')
def delete_repair(request):
    return delete_view(request, models.Repair)
