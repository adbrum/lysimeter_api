# Generated by Django 2.2.3 on 2020-04-09 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lysimeter', '0003_auto_20200409_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceparams',
            name='date_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=17),
            preserve_default=False,
        ),
    ]
