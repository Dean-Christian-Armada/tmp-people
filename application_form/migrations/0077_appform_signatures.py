# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0076_remove_appform_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='appform',
            name='signatures',
            field=models.ImageField(default=None, upload_to=b'signatures'),
        ),
    ]
