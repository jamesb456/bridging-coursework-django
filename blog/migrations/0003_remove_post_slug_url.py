# Generated by Django 2.2.12 on 2020-07-31 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug_url',
        ),
    ]
