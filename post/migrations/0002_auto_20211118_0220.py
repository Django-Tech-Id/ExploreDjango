# Generated by Django 2.2.10 on 2021-11-18 02:20

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post/post.jpg', null=True, upload_to=post.models.upload_location),
        ),
    ]