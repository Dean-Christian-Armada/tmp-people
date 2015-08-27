# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0058_auto_20150827_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentaddress',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='availability_date',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_1',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='landline_2',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='dwt',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='grt',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='hp',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='kw',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='seaservice',
            name='year_built',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yellowfever',
            name='yellow_fever',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
