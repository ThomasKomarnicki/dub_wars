# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_battler', '0002_auto_20151129_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songbattle',
            name='winner',
            field=models.IntegerField(default=-1),
        ),
    ]
