# Generated by Django 2.1.2 on 2018-11-30 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20181123_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]