# Generated by Django 3.0.5 on 2020-04-20 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='socialmedia',
            unique_together={('user', 'source', 'identifier')},
        ),
    ]
