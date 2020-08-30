# Generated by Django 2.2.12 on 2020-08-28 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0016_auto_20200828_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='skill',
            name='end_date',
            field=models.DateField(default=datetime.date(1970, 1, 2)),
        ),
        migrations.AddField(
            model_name='skill',
            name='start_date',
            field=models.DateField(default=datetime.date(1970, 1, 1)),
        ),
    ]