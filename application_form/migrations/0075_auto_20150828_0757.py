# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0074_auto_20150828_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appform',
            name='background_information',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='certificates_documents',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='education',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='emergency_contact',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='reference',
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='flag',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
