# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0038_auto_20150819_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsource',
            name='source',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
