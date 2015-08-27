# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0060_auto_20150827_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentaddress',
            old_name='baranggay',
            new_name='current_baranggay',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='municipality',
            new_name='current_municipality',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='street',
            new_name='current_street',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='town',
            new_name='current_town',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='baranggay',
            new_name='permanent_baranggay',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='municipality',
            new_name='permanent_municipality',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='street',
            new_name='permanent_street',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='town',
            new_name='permanent_town',
        ),
    ]
