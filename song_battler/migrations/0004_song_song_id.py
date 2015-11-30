# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_battler', '0003_auto_20151129_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_id',
            field=models.CharField(default='0', max_length=32),
            preserve_default=False,
        ),
    ]
