# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


OBJECT_ROW = """<tr id="object-{id}">
    <td>
        {counter}
    </td>
    <td>
        {client}
    </td>
    <td>
        {employee}
    </td>
    <td>
        {order_date}
    </td>
    <td>
        {receipt_date}
    </td>
    <td>
        {price}
    </td>
    <td>
        {description}
    </td>
    <td>
        <a href="{url_display}">
            <i class="glyphicon glyphicon-share-alt"></i>
        </a>
        {super}
    </td>
</tr>
"""

SUPERUSER = """
<a href="{url_edit}">
    <i class="glyphicon glyphicon-pencil"></i>
</a>
<span class="text-danger">
    <i class="glyphicon glyphicon-trash removeObject" data-id="{id}" data-toggle="modal" data-target="#deleteModal" title="{title}"></i>
</span>
"""




def generate_row(object, counter, client):
    url_display = reverse('repair_display', kwargs={'repair_id': object.id})
    url_edit = reverse('repair_edit', kwargs={'repair_id': object.id})
    if client:
        super = ""
    else:
        super = SUPERUSER.format(url_edit=url_edit, title=_("Delete repair"),
                                 id=object.id)
    return OBJECT_ROW.format(id=object.id, counter=counter,
                             client=unicode(object.client),
                             employee=unicode(object.employee),
                             order_date=object.order_date,
                             receipt_date=object.receipt_date,
                             price=object.price, url_display=url_display,
                             description=object.description,
                             super=super)
