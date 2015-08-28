# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0079_auto_20150828_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='contact',
            new_name='emeregency_contact',
        ),
        migrations.RenameField(
            model_name='spouse',
            old_name='contact',
            new_name='spouse_contact',
        ),
    ]
