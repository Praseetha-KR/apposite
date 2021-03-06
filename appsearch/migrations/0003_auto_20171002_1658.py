# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsearch', '0002_app_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='appid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='app',
            name='current_version',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='icon',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='app',
            name='review_count',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='supported_os',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='total_downloads',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='email',
            field=models.EmailField(default='admin@localhost', max_length=254),
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
