# Generated by Django 2.2.12 on 2020-08-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_slug_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
