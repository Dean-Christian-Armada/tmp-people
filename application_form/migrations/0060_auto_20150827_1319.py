# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0059_auto_20150827_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='married_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
