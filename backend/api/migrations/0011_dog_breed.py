# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180927_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Breed'),
        ),
    ]
