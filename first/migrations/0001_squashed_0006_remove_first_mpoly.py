# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    replaces = [(b'first', '0001_initial'), (b'first', '0002_auto_20141103_1548'), (b'first', '0003_first_ip'), (b'first', '0004_first_mpoly'), (b'first', '0005_auto_20141228_1030'), (b'first', '0006_remove_first_mpoly')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('created', models.DateField(default=datetime.date(2014, 11, 3), auto_now_add=True)),
                ('modified', models.DateTimeField(default=datetime.date(2014, 11, 3), auto_now=True)),
                ('ip', models.GenericIPAddressField(default='0.0.0.0', protocol=b'IPv4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
