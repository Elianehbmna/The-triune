# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-08 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20191008_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
