# Generated by Django 2.2.12 on 2020-08-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='email',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
    ]