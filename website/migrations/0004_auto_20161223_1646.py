# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-23 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161221_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctacte',
            name='afected_date',
            field=models.DateField(null=True, verbose_name='Fecha Afectado'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='date_1',
            field=models.DateField(null=True, verbose_name='Fecha 1'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='date_2',
            field=models.DateField(null=True, verbose_name='Fecha 2'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='exchange_rate_adjustment_date',
            field=models.DateField(null=True, verbose_name='Fecha Ajuste de Cambio'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='voucher_date',
            field=models.DateField(null=True, verbose_name='Fecha Comprobante'),
        ),
    ]