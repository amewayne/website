# Generated by Django 3.1.6 on 2021-02-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
    ]
