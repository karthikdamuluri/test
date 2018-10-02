# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 22:23
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='excerciseneeds',
            field=models.IntegerField(validators=[api.models.validate_number]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendlyness',
            field=models.IntegerField(validators=[api.models.validate_number]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddinamount',
            field=models.IntegerField(validators=[api.models.validate_number]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(validators=[api.models.validate_number]),
        ),
    ]
