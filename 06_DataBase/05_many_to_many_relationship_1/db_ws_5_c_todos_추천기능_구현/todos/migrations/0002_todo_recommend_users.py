# Generated by Django 4.2.11 on 2024-04-07 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='recommend_users',
            field=models.ManyToManyField(related_name='recommend_todos', to=settings.AUTH_USER_MODEL),
        ),
    ]
