# Generated by Django 4.2.1 on 2023-06-12 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0010_booking_xray'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phoneno', models.IntegerField()),
                ('bld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.blood_category')),
            ],
        ),
    ]
