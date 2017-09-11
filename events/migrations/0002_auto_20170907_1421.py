# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='visibility',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='eventinvitations',
            name='response_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventinvitations',
            name='status',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]