# Generated by Django 3.1.5 on 2022-06-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendinghandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='imageName',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
