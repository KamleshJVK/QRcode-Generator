# Generated by Django 5.0.7 on 2024-08-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0002_alter_destination_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
