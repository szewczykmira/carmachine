# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

OBJECT_ROW = """<tr id="object-{id}">
    <td>
        {counter}
    </td>
    <td>
        {name}
    </td>
    <td>
        {address}
    </td>
    <td>
        {telephone}
    </td>
    <td>
        {email}
    </td>
    <td>
        {description}
    </td>
    <td>
        {nip}
    </td>
    <td>
        {regon}
    </td>
    <td>
        <a href="{url}">
            <i class="glyphicon glyphicon-pencil"></i>
        </a>
        <span class="text-danger">
            <i class="glyphicon glyphicon-trash removeObject" data-id="{id}" data-toggle="modal" data-target="#deleteModal" title="{title}"></i>
        </span>
    </td>
</tr>
"""


def generate_row(object, counter):
    url = reverse('provider_edit', kwargs={'provider': object.id})
    return OBJECT_ROW.format(
        id=object.id, counter=counter, name=object.name,
        address=object.address, description=object.description,
        telephone=object.telephone, email=object.email, url=url,
        title=_("Delete employee"), nip=object.nip, regon=object.regon)
