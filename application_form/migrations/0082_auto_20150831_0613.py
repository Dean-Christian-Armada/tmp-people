# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0081_auto_20150828_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='civil_status',
            field=models.CharField(default=None, max_length=50, choices=[(b'Civil Status', b'Civil Status'), (b'M', b'Married'), (b'S', b'Single'), (b'LS', b'Legally Separated'), (b'W', b'Widow')]),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='pagibig',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='philhealth',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='sss',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='tin',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
