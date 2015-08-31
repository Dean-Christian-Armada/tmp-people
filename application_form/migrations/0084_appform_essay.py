# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0083_remove_appform_essay'),
    ]

    operations = [
        migrations.AddField(
            model_name='appform',
            name='essay',
            field=models.TextField(default=None),
        ),
    ]
