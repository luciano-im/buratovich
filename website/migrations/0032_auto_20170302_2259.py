# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-03 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20170302_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rain',
            name='id',
        ),
        migrations.AlterField(
            model_name='rain',
            name='date',
            field=models.DateField(primary_key=True, serialize=False, verbose_name='Fecha'),
        ),
    ]
