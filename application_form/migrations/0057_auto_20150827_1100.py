# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0056_auto_20150820_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appdetails',
            old_name='appdetails',
            new_name='appsource',
        ),
    ]
