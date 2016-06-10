# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account
import json


def delete_view(request, model):
    if Account.objects.get_from_user(request.user).is_client() or \
            not request.user.is_active:
        raise Http404(_("This is not the road you are looking for!"))
    if request.method == 'POST' and request.is_ajax():
        try:
            object = model.objects.get(id=request.POST['object_id'])
            object.delete()
            success = True
        except model.DoesNotExist:
            success = False
        return HttpResponse(json.dumps({'success': success}),
                            content_type='application/json')