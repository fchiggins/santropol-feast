# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_auto_20160506_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencing',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 12), verbose_name='referral_date'),
        ),
    ]
