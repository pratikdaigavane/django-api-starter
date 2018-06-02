# Generated by Django 2.0 on 2018-06-02 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255)),
                ('page', models.CharField(max_length=255)),
                ('value', models.TextField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together={('identifier', 'page')},
        ),
    ]
