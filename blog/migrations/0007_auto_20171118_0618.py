# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_train_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='date',
            field=models.CharField(default='2017-11-18', max_length=256, verbose_name='date'),
        ),
    ]
