# Generated by Django 5.0 on 2023-12-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_event_photo_alter_event_id_alter_recevoir_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='codebare',
            field=models.ImageField(default='', upload_to='image/'),
            preserve_default=False,
        ),
    ]