# Generated by Django 4.2.1 on 2023-06-11 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_blood_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=70)),
                ('phoneno', models.IntegerField()),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.category')),
            ],
        ),
    ]
