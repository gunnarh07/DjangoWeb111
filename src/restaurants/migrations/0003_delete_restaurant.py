# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-25 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_locations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
