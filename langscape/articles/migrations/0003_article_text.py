# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
