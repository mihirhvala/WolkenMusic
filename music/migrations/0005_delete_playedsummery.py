# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-19 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_playedsummery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayedSummery',
        ),
    ]