# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pro_icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=50, verbose_name='\u4ea7\u54c1\u56fe\u6807')),
                ('photo', models.ImageField(default='protemp.jpg', upload_to='photos')),
            ],
        ),
    ]
