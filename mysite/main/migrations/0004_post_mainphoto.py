# Generated by Django 2.1.8 on 2019-05-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
