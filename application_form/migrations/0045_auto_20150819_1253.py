# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0044_auto_20150819_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='civil_status',
            field=models.CharField(max_length=50, null=True, choices=[(b'Civil Status', b'Civil Status'), (b'M', b'Married'), (b'S', b'Single')]),
        ),
    ]
