# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-05 12:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='author_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='author_name',
            new_name='name',
        ),
    ]
