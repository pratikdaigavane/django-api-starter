# Generated by Django 2.1.7 on 2019-04-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190404_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='source',
            field=models.IntegerField(choices=[(0, 'Facebook'), (1, 'Google')], db_index=True, default=0),
        ),
        migrations.AlterUniqueTogether(
            name='socialmedia',
            unique_together={('user', 'source', 'identifier')},
        ),
    ]
