# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 14:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_auto_20160506_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(blank='True', default=django.utils.timezone.now, null='True'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank='True', choices=[('M', 'male'), ('F', 'female'), ('U', 'unknown')], default='U', max_length=1, null='True'),
        ),
        migrations.AlterField(
            model_name='referencing',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 13), verbose_name='referral_date'),
        ),
    ]