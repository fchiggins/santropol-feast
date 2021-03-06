# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 19:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0009_referencing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='text_note')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='creation_date')),
                ('is_read', models.BooleanField(default=False, verbose_name='is_read')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name_plural': 'notes',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='member.Member', verbose_name='member'),
        ),
    ]
