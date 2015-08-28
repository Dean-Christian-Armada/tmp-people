# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0077_appform_signatures'),
    ]

    operations = [
        migrations.AddField(
            model_name='appform',
            name='background_information',
            field=models.OneToOneField(default=None, to='application_form.BackgroundInformation'),
        ),
        migrations.AddField(
            model_name='appform',
            name='certificates_documents',
            field=models.OneToOneField(default=None, to='application_form.CertificatesDocuments'),
        ),
        migrations.AddField(
            model_name='appform',
            name='education',
            field=models.OneToOneField(default=None, to='application_form.Education'),
        ),
        migrations.AddField(
            model_name='appform',
            name='emergency_contact',
            field=models.OneToOneField(default=None, to='application_form.EmergencyContact'),
        ),
        migrations.AddField(
            model_name='appform',
            name='personal_data',
            field=models.OneToOneField(default=None, to='application_form.PersonalData'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='signatures',
            field=models.ImageField(default=None, upload_to=b'signatures', blank=True),
        ),
    ]
