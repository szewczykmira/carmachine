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
        {producent}
    </td>
    <td>
        {description}
    </td>
    <td>
        {price}
    </td>
    <td>
        {quantity}
    </td>
    <td>
        <a href="{url}">
            <i class="glyphicon glyphicon-pencil"></i>
        </a>
        <span class="text-danger">
            <i class="glyphicon glyphicon-trash removeObject" data-id="{id}"
            data-toggle="modal" data-target="#deleteModal" title="{title}"></i>
        </span>
    </td>
</tr>"""


def generate_row(object, counter):
    url = reverse('carpart_edit', kwargs={'partid': 5})
    return OBJECT_ROW.format(
        id=object.id, counter=counter, name=object.name,
        producent=object.producent, description=object.description,
        price=object.price, quantity=object.quantity, url=url,
        title=_("Delete employee"))
