# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-03 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.TextField()),
                ('user', models.TextField()),
                ('time', models.DateField(blank=True, null=True)),
                ('input_lan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='S3store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.TextField()),
                ('source_url', models.TextField()),
                ('output_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Translatioin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.TextField()),
                ('result', models.TextField()),
                ('output_lan', models.TextField()),
            ],
        ),
    ]
