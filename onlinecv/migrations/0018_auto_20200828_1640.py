# Generated by Django 2.2.12 on 2020-08-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0017_auto_20200828_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='start_date',
        ),
    ]