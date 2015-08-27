# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0061_auto_20150827_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentaddress',
            old_name='zip',
            new_name='current_zip',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='zip',
            new_name='permanent_zip',
        ),
    ]
