# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0088_auto_20150831_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='flags',
            field=models.ManyToManyField(to='application_form.FlagDocuments', blank=True),
        ),
    ]
