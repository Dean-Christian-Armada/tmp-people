# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0078_auto_20150828_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spouse',
            old_name='name',
            new_name='spouse_name',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='name',
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='emergency_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='appform',
            name='background_information',
            field=models.OneToOneField(to='application_form.BackgroundInformation'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='certificates_documents',
            field=models.OneToOneField(to='application_form.CertificatesDocuments'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='education',
            field=models.OneToOneField(to='application_form.Education'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='emergency_contact',
            field=models.OneToOneField(to='application_form.EmergencyContact'),
        ),
        migrations.AlterField(
            model_name='appform',
            name='personal_data',
            field=models.OneToOneField(to='application_form.PersonalData'),
        ),
    ]
