# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from accounts.models import Account
from CarMachine.helper_views import home_view, delete_view
import json


@login_required(login_url='/accounts/login')
def home(request):
    return home_view(request, models.Order, 'order/index.html')


@login_required(login_url='/accounts/login')
def add_order(request, order_id=None):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))

    if order_id:
        order = get_object_or_404(models.Order, id=order_id)
        form = forms.OrderForm(request.POST or None, instance=order)
    else:
        form = forms.OrderForm(request.POST or None)

    context = {'form': form}
    if request.method == 'POST':
        if context['form'].is_valid():
            order = context['form'].save()
            messages.success(request, _('Order has been added'))
            return redirect(reverse('order_display',
                                    kwargs={'order_id': order.id}))
        messages.error(request, _("Please review information!"))

    return render(request, 'order/add_order.html', context)


@login_required(login_url='/accounts/login')
def delete_order(request):
    return delete_view(request, models.Order)


@login_required(login_url='/accounts/login')
def display_order(request, order_id):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        return Http404(_("You are not allowed to be here!"))

    context = {'order': get_object_or_404(models.Order, id=order_id)}
    return render(request, 'order/display_order.html', context)
