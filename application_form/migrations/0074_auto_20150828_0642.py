# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0073_personaldata_training_certificates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaservice',
            name='cause_of_discharge',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='date_joined',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='date_left',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='duration',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='engine_type',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='grt',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='manning_agency',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='principal',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='rank',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='vessel_name',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='vessel_type',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='year_built',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
