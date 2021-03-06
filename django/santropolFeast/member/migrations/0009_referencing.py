# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 19:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20160423_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_reason', models.TextField(verbose_name='referral_reason')),
                ('date', models.DateField(default=datetime.date(2016, 4, 27), verbose_name='referral_date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Client', verbose_name='client')),
                ('referent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member', verbose_name='referent')),
            ],
            options={
                'verbose_name_plural': 'referents',
            },
        ),
    ]
