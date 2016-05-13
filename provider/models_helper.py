# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def validate_nip(nip):
    ratio_list = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    add = sum(map(
        lambda (x, y): x*int(y),
        zip(ratio_list, nip)))
    if not int(nip[-1]) == add % 11:
        raise ValidationError(_("It's not valid NIP!"))

def validate_regon(regon):
    ratio_list = [8, 9, 2, 3, 4, 5, 6, 7]
    add = sum(map(
        lambda (x, y): x*int(y),
        zip(ratio_list, regon)))

    if not (add % 11) % 10 == int(regon[-1]):
        raise ValidationError(_("It's not valid REGON"))


