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
from CarMachine.helper_views import delete_view
import json


@login_required(login_url='accounts/login')
def home(request):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))
    context = {
        'objects': models.Provider.objects.all()
    }
    return render(request, 'provider/index.html', context)


@login_required(login_url='accounts/login')
def add_provider(request, provider=None):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))
    if provider:
        provider = models.Provider.objects.get(id=provider)
        form = forms.ProviderForm(request.POST or None, instance=provider)
    else:
        form = forms.ProviderForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if context['form'].is_valid():
            provider = context['form'].save()
            messages.success(request, _('Provider has been added'))
            return redirect('provider_home')
        messages.error(request, _("Please review information!"))

    return render(request, 'provider/provider_add.html', context)


@login_required(login_url='accounts/login')
def delete_provider(request):
    return delete_view(request, models.Provider)


@login_required(login_url='accounts/login')
def get_providers(request):
    if Account.objects.get_from_user(request.user).is_client() or\
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    search_val = request.GET['input']
    objects = models.Provider.objects.filter(
        Q(name__icontains=search_val))
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
