# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('producent', models.CharField(max_length=100, verbose_name='Producent')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
            ],
        ),
    ]
