# Generated by Django 2.1.3 on 2018-11-11 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181111_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttexts',
            old_name='post_id',
            new_name='post',
        ),
    ]
