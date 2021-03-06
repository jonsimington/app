# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.teams.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20150907_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(help_text=b"Your team's project name!", max_length=50, validators=[django.core.validators.RegexValidator(regex=b'[a-zA-Z0-9_\\-.:\\s]+', message=b'Names can contain letters, numbers, dashes, periods, colons, and whitespace.'), project.teams.models.slug_validator]),
        ),
    ]
