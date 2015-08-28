# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0067_auto_20150828_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificatesdocuments',
            old_name='schgengen_visa',
            new_name='schengen_visa',
        ),
    ]
