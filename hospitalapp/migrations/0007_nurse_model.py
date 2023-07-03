# Generated by Django 4.2.1 on 2023-06-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0006_add_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='nurse_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=70)),
                ('phoneno', models.IntegerField()),
            ],
        ),
    ]
