# Generated by Django 5.0 on 2023-12-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lieu', models.CharField(max_length=128)),
                ('event_date', models.DateTimeField()),
                ('event_photo', models.ImageField(upload_to='image/')),
                ('nbr_ticket', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Recevoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(upload_to='image/')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
