# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-11 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20180811_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksheet',
            name='enroll_number',
        ),
        migrations.AlterField(
            model_name='marksheet',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marksheets', to='accounts.Profile'),
        ),
    ]
