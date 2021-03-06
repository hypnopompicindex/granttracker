# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0005_auto_20170713_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'schedules',
            },
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='grant',
            new_name='schedule',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='grants.Grant'),
        ),
    ]
