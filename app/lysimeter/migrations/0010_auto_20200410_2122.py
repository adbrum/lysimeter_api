# Generated by Django 2.2.3 on 2020-04-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lysimeter', '0009_auto_20200410_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceparams',
            name='date_time',
            field=models.CharField(max_length=20),
        ),
    ]