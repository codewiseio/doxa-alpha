# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-06 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_involvement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='involvement',
            field=models.IntegerField(default=0),
        ),
    ]
