# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models, forms
from .helpers import generate_row, generate_item_row
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
        raise Http404(_("You are not allowed to be here!"))

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
def delete_repair(request, repair_id=None):
    if not repair_id:
        return delete_view(request, models.Repair)
    repair = get_object_or_404(models.Repair, id=repair_id)
    repair.get_items().delete()
    repair.delete()
    messages.success(request, _("Repair has been deleted"))
    return redirect('home_page')


@login_required(login_url='/accounts/login')
def get_repairs(request):
    if not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))

    if Account.objects.get_from_user(request.user).is_client():
        objects = models.Repair.objects.filter(client__account=request.user)
        client = True
    else:
        objects = models.Repair.objects.all()
        client = False
    search_val = request.GET['input']
    objects = objects.filter(
        Q(client__account__username__icontains=search_val) |
        Q(client__account__last_name__icontains=search_val) |
        Q(client__account__first_name__icontains=search_val) |
        Q(employee__account__username__icontains=search_val) |
        Q(employee__account__first_name__icontains=search_val) |
        Q(employee__account__last_name__icontains=search_val))
    if bool(request.GET['sort']):
        objects = objects.order_by(request.GET['sort'])
    row_list = []
    i = 1
    for elem in objects:
        row_list.append(generate_row(elem, i, client))
        i += 1
    context = {
        'objects': row_list,
    }
    return HttpResponse(json.dumps(context), content_type='application/json')


@login_required(login_url='/accounts/login')
def display_repair(request, repair_id):
    if not request.user.is_active:
        raise Http404(_("You are not allowed to be here!"))

    repair = get_object_or_404(models.Repair, pk=repair_id)

    if Account.objects.get_from_user(request.user).is_client() \
            and not repair.client == request.user.client:
        raise Http404(_("You are not allowed to be here!"))

    context = {'repair': repair,
               'form': forms.RepairItemForm()}
    context['items'] = context['repair'].get_items()
    return render(request, 'repair/display_repair.html', context)


@login_required(login_url='/accounts/login')
def add_items(request, repair_id):
    if Account.objects.get_from_user(request.user).is_client() or\
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    if request.method == 'POST' and request.is_ajax():
        repair = get_object_or_404(models.Repair, pk=repair_id)
        form = forms.RepairItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.repair = repair
            item.save()
            context = {'row': generate_item_row(item,
                                                repair.get_items().count()),
                       'success': True}
        else:
            context = {'success': False}

        return HttpResponse(json.dumps(context),
                            content_type='appliaction/json')

    return HttpResponse("Something went wrong")


@login_required(login_url='/accounts/login')
def delete_items(request):
    return delete_view(request, models.RepairItem)