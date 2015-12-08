# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_battler', '0004_song_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='elo',
            field=models.IntegerField(default=0),
        ),
    ]
