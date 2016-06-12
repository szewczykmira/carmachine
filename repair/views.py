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
