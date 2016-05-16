# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import provider.models_helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('telephone', models.CharField(max_length=9, verbose_name='Telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail address')),
                ('description', models.TextField(verbose_name='Descritpion')),
                ('nip', models.CharField(blank=True, max_length=10, null=True, validators=[provider.models_helper.validate_nip], verbose_name='NIP')),
                ('regon', models.CharField(blank=True, max_length=9, null=True, validators=[provider.models_helper.validate_regon], verbose_name='REGON')),
            ],
        ),
    ]
