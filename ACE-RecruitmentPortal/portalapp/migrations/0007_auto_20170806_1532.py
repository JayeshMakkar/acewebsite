# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_auto_20170806_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aceuserprofile',
            name='course',
            field=models.CharField(default=None, max_length=3),
        ),
    ]
