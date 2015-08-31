# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0084_appform_essay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentaddress',
            name='current_town',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='emergency_town',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='permanent_town',
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthdate',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='spouse_contact',
            field=models.IntegerField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='spouse_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
