# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-12 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180312_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='specs',
            name='sales_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
    ]
