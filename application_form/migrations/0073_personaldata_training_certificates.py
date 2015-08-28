# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0072_remove_personaldata_training_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='training_certificates',
            field=models.ManyToManyField(to='application_form.TrainingCertificates'),
        ),
    ]
