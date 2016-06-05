# -*- coding: utf-8 -*-

from django.db import models


class AccountManager(models.Manager):
    def get_from_user(self, user):
        return self.get(id=user.id)
