# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from .helpers import generate_row_order
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


@login_required(login_url='/accounts/login')
def get_orders(request):
    if Account.objects.get_from_user(request.user).is_client() or\
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    search_val = request.GET['input']
    objects = models.Order.objects.filter(provider__name__icontains=search_val)
    if bool(request.GET['sort']):
        objects = objects.order_by(request.GET['sort'])
    row_list = []
    i = 1
    for elem in objects:
        row_list.append(generate_row_order(elem, i))
        i += 1
    context = {
        'objects': row_list,
    }
    return HttpResponse(json.dumps(context), content_type='application/json')
