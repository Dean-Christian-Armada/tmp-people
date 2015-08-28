# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0071_auto_20150828_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='training_certificates',
        ),
    ]
