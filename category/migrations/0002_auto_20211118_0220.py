# Generated by Django 2.2.10 on 2021-11-18 02:20

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=category.models.upload_location),
        ),
    ]