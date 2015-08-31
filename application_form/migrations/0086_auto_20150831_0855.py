# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0085_auto_20150831_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='emergency_contact',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='spouse_contact',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
