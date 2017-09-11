# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-10 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_auto_20170909_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='municipality',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='postcode',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='telephone',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]