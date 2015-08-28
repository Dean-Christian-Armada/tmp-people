# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_form', '0065_auto_20150827_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coc',
            old_name='expiry',
            new_name='coc_expiry',
        ),
        migrations.RenameField(
            model_name='coc',
            old_name='rank',
            new_name='coc_rank',
        ),
        migrations.RenameField(
            model_name='goc',
            old_name='expiry',
            new_name='goc_expiry',
        ),
        migrations.RenameField(
            model_name='license',
            old_name='rank',
            new_name='license_rank',
        ),
        migrations.RenameField(
            model_name='passport',
            old_name='expiry',
            new_name='passport_expiry',
        ),
        migrations.RenameField(
            model_name='passport',
            old_name='place',
            new_name='passport_place',
        ),
        migrations.RenameField(
            model_name='sbook',
            old_name='expiry',
            new_name='sbook_expiry',
        ),
        migrations.RenameField(
            model_name='sbook',
            old_name='place',
            new_name='sbook_place',
        ),
        migrations.RenameField(
            model_name='schengenvisa',
            old_name='expiry',
            new_name='schengen_expiry',
        ),
        migrations.RenameField(
            model_name='schengenvisa',
            old_name='type',
            new_name='schengen_type',
        ),
        migrations.RenameField(
            model_name='src',
            old_name='rank',
            new_name='src_rank',
        ),
        migrations.RenameField(
            model_name='usvisa',
            old_name='expiry',
            new_name='usvisa_expiry',
        ),
        migrations.RenameField(
            model_name='usvisa',
            old_name='type',
            new_name='usvisa_type',
        ),
        migrations.RenameField(
            model_name='yellowfever',
            old_name='expiry',
            new_name='yellow_fever_expiry',
        ),
    ]
