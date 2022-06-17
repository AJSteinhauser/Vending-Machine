# Generated by Django 3.1.5 on 2022-06-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('userPassword', models.CharField(blank=True, max_length=255, null=True)),
                ('userCash', models.DecimalField(decimal_places=2, default=100.0, max_digits=5)),
            ],
        ),
    ]