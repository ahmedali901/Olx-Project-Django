# Generated by Django 3.0.7 on 2020-06-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
