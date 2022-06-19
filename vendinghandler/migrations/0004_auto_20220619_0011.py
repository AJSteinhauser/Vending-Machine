# Generated by Django 3.1.5 on 2022-06-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendinghandler', '0003_auto_20220617_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
        ),
    ]
