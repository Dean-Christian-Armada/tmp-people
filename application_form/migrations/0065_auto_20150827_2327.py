# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0064_auto_20150827_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='school',
            new_name='college',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='school',
            new_name='highschool',
        ),
    ]
