# Generated by Django 4.2.1 on 2023-06-25 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0017_bookings_model_appoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings_model',
            name='appoint',
        ),
    ]