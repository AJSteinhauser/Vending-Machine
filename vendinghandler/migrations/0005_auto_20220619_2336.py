# Generated by Django 3.1.5 on 2022-06-19 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendinghandler', '0004_auto_20220619_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='inStock',
            field=models.IntegerField(default=50),
        ),
    ]
