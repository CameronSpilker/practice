# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 00:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20170423_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='qoute',
            new_name='quote',
        ),
    ]