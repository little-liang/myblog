# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_article_viwes_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_summary',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]