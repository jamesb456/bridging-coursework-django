# Generated by Django 2.2.12 on 2020-08-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0002_cv_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
