# Generated by Django 2.2.12 on 2020-08-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0006_cv_linkedin_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='personal_statement',
            field=models.TextField(default=''),
        ),
    ]