# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-24 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20170224_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='old_user',
            field=models.BooleanField(default=False),
        ),
    ]
