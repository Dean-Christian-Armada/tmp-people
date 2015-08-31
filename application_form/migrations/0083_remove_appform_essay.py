# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0082_auto_20150831_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appform',
            name='essay',
        ),
    ]
