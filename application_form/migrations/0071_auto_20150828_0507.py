# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0070_auto_20150828_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appform',
            name='flags',
        ),
        migrations.RemoveField(
            model_name='appform',
            name='training_certificates',
        ),
        migrations.RemoveField(
            model_name='seaservice',
            name='app_form',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='flags',
            field=models.ManyToManyField(to='application_form.FlagDocuments'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='training_certificates',
            field=models.ManyToManyField(to='application_form.TrainingCertificates'),
        ),
        migrations.AddField(
            model_name='seaservice',
            name='personal_data',
            field=models.ForeignKey(default=None, to='application_form.PersonalData'),
        ),
    ]
