# Generated by Django 3.2.9 on 2022-08-15 21:17

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api03', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='dog',
            managers=[
                ('mm', django.db.models.manager.Manager()),
            ],
        ),
    ]
