# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20171103_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='is_internal',
            new_name='is_main',
        ),
    ]
