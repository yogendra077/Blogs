# Generated by Django 4.0.6 on 2022-07-10 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
