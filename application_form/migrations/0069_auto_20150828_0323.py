# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0068_auto_20150828_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schengenvisa',
            name='schengen_type',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='usvisa',
            name='usvisa_type',
            field=models.NullBooleanField(),
        ),
    ]
