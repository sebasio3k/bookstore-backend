# Generated by Django 4.1 on 2022-08-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_created_at_author_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='imagen'),
        ),
    ]