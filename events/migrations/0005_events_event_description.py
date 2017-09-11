# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_description',
            field=models.TextField(default=b'hello'),
            preserve_default=True,
        ),
    ]
