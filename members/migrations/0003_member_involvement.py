# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20170212_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='involvement',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]