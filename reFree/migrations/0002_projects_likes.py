# Generated by Django 3.1.2 on 2020-10-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reFree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
