# Generated by Django 4.2.7 on 2024-02-05 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy_file_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='filerequest',
            old_name='user_id',
            new_name='user',
        ),
    ]
