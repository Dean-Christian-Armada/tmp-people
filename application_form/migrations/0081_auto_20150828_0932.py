# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0080_auto_20150828_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='baranggay',
            new_name='emergency_baranggay',
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='emeregency_contact',
            new_name='emergency_contact',
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='municipality',
            new_name='emergency_municipality',
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='street',
            new_name='emergency_street',
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='town',
            new_name='emergency_town',
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='zip',
            new_name='emergency_zip',
        ),
    ]
