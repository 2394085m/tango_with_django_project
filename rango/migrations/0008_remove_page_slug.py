# Generated by Django 2.1.5 on 2020-02-14 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20200214_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
