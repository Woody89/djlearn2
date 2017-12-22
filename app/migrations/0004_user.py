# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-22 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_imitate'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]