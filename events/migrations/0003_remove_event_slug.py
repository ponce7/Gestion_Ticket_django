# Generated by Django 5.0 on 2023-12-14 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_nbr_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
