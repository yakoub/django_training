# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='paragraphs',
        ),
        migrations.AddField(
            model_name='paragraph',
            name='article',
            field=models.ForeignKey(default=0, to='article.Article'),
            preserve_default=False,
        ),
    ]
