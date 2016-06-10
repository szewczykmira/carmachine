# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from accounts.models import Account
from CarMachine.helper_models import delete_view


@login_required(login_url='accounts/login')
def home(request):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))
    context = {
        'objects': models.Provider.objects.all()
    }
    print context
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
