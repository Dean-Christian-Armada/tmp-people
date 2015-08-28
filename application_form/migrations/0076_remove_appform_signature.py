# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0075_auto_20150828_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appform',
            name='signature',
        ),
    ]
