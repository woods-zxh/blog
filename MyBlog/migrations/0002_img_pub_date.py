# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]