# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokersessions', '0004_auto_20161216_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokersession',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
