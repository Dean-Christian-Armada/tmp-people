# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0066_auto_20150828_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passport',
            name='passport_place',
        ),
        migrations.RemoveField(
            model_name='sbook',
            name='sbook_place',
        ),
    ]
