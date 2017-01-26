# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-20 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170120_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctacte',
            name='address_apartment',
            field=models.CharField(max_length=10, verbose_name='Depto.'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='address_number',
            field=models.CharField(max_length=10, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='C\xf3digo Postal'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='postal_sufix',
            field=models.CharField(max_length=10, verbose_name='Sufijo'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='tax_address_apartment',
            field=models.CharField(max_length=10, verbose_name='Depto. Dom. Fiscal'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='tax_address_number',
            field=models.CharField(max_length=10, verbose_name='Numero Dom. Fiscal'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='tax_posta_sufix',
            field=models.CharField(max_length=10, verbose_name='Sufijo Postal Fiscal'),
        ),
        migrations.AlterField(
            model_name='ctacte',
            name='tax_postal_code',
            field=models.CharField(max_length=10, verbose_name='C\xf3digo Postal Fiscal'),
        ),
    ]