# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0086_auto_20150831_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='mobile_1',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
