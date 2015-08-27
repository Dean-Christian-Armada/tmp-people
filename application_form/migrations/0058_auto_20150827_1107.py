# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0057_auto_20150827_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appsource',
            old_name='specify',
            new_name='specific',
        ),
    ]
