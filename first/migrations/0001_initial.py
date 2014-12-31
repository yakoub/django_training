# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField(protocol=b'IPv4')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
