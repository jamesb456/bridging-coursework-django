# Generated by Django 2.2.12 on 2020-08-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0007_cv_personal_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='github_profile',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='cv',
            name='linkedin_profile',
            field=models.URLField(default=''),
        ),
    ]
