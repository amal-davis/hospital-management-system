# Generated by Django 4.2.1 on 2023-06-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_book_blood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_blood',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book_blood',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking_labs',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking_labs',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking_xray',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking_xray',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
    ]