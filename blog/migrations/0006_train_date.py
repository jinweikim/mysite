# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=256, verbose_name='date'),
            preserve_default=False,
        ),
    ]
