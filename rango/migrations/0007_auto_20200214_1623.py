# Generated by Django 2.1.5 on 2020-02-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(),
        ),
    ]
