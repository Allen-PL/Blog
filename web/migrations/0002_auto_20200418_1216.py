# Generated by Django 2.2.5 on 2020-04-18 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content_md',
            new_name='content',
        ),
    ]
