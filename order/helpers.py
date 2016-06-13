# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

OBJECT_ROW = """<tr id="object-{id}">
    <td>
        {counter}
    </td>
    <td>
        <a href="{url_display}">
            {provider}
        </a>
    </td>
    <td>
        {price}
    </td>
    <td>
        {order_date}
    </td>
    <td>
        {receipt_date}
    </td>
    <td>
        <a href="{url_edit}">
            <i class="glyphicon glyphicon-pencil"></i>
        </a>
        <span class="text-danger">
            <i class="glyphicon glyphicon-trash removeObject" data-id="{id}" data-toggle="modal" data-target="#deleteModal" title="{title}"></i>
        </span>
    </td>
</tr>
"""

ITEM_ROW = """<tr id="object-{id}">
    <td>
        {counter}
    </td>
    <td>
        {cart_part}
    </td>
    <td>
        {price}
    </td>
    <td>
        <span class="text-danger">
            <i class="glyphicon glyphicon-trash removeObject" data-id="{id}" data-toggle="modal" data-target="#deleteModal"></i>
        </span>
    </td>
</tr>
"""


def generate_row_order(object, counter):
    url_edit = reverse('order_edit', kwargs={'order_id': object.id})
    url_display = reverse('order_display', kwargs={'order_id': object.id})
    return OBJECT_ROW.format(
        id=object.id, counter=counter, url_display=url_display,
        price=object.price, order_date=object.order_date,
        receipt_date=object.receipt_date, url_edit=url_edit,
        title=_("Delete order"), provider=object.provider)


def generate_row_item(object, counter):
    return ITEM_ROW.format(id=object.id, counter=counter,
                           cart_part=object.cart_part, price=object.price)
