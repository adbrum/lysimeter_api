# Generated by Django 2.2.3 on 2020-04-10 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lysimeter', '0005_auto_20200409_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceparams',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
