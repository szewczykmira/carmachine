# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from . import models
from accounts.models import Account
from CarMachine.helper_views import home_view
import json


@login_required(login_url='/accounts/login')
def home(request):
    return home_view(request, models.Order, 'order/index.html')
