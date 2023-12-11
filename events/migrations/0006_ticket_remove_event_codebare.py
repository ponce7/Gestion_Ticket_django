# Generated by Django 5.0 on 2023-12-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_codebare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codebare', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='codebare',
        ),
    ]
