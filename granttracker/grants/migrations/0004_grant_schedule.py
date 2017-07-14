# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0003_grant_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='schedule',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='grants.Schedule'),
        ),
    ]
