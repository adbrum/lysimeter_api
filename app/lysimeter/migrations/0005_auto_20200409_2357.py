# Generated by Django 2.2.3 on 2020-04-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lysimeter', '0004_deviceparams_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceparams',
            name='created_at',
            field=models.DateTimeField(verbose_name='2020-04-09 23:57:04'),
        ),
    ]