# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20171025_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='my_date_field',
        ),
    ]
