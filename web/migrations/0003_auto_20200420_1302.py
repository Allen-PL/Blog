# Generated by Django 2.2.5 on 2020-04-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200418_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.TextField(default='aa', verbose_name='简介'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='skill',
            field=models.TextField(default='aa', verbose_name='技能'),
            preserve_default=False,
        ),
    ]