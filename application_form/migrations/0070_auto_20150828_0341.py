# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0069_auto_20150828_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundinformation',
            name='detained',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='backgroundinformation',
            name='disciplinary_action',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='backgroundinformation',
            name='visa_application',
            field=models.NullBooleanField(),
        ),
    ]
