# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-02-20 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_ticketsanalysis_speciesharvest'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsanalysis',
            name='algoritmo_code',
            field=models.IntegerField(default=0, verbose_name='Cuenta Algoritmo'),
            preserve_default=False,
        ),
    ]
