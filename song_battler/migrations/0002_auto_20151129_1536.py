# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_battler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(default=1),
        ),
    ]
