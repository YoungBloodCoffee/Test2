# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160929_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='FK_Favorite',
        ),
        migrations.AddField(
            model_name='add_favorite',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='home.Quotes'),
        ),
    ]
