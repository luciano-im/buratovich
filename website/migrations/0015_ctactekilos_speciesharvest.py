# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-31 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20170125_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctactekilos',
            name='speciesharvest',
            field=models.CharField(max_length=8, null=True, verbose_name='Especie Cosecha'),
        ),
    ]
