# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0087_auto_20150831_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='emergency_contact',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='spouse_contact',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
