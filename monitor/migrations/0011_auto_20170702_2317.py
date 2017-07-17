# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20170702_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test_email',
            field=models.BooleanField(default=False, help_text='Please check if you want to test email alert.'),
        ),
        migrations.AddField(
            model_name='profile',
            name='test_telegram',
            field=models.BooleanField(default=False, help_text='Please check if you want to test telegram alert.'),
        ),
    ]