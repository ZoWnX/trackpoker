# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20161225_0119'),
        ('locations', '0002_auto_20170101_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='games',
            field=models.ManyToManyField(to='games.Game'),
        ),
    ]
