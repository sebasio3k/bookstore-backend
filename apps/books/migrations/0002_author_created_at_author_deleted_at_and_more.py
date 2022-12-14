# Generated by Django 4.1 on 2022-08-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
