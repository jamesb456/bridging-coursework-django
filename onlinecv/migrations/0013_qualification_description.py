# Generated by Django 2.2.12 on 2020-08-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0012_qualification_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='description',
            field=models.TextField(default=''),
        ),
    ]