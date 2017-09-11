# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_events_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_price',
            field=models.DecimalField(default=1000.0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='events',
            name='users_bought',
            field=models.TextField(default=1000.0),
            preserve_default=False,
        ),
    ]
