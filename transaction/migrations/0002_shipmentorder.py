# Generated by Django 3.1.3 on 2021-01-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipmentId', models.CharField(max_length=6)),
            ],
        ),
    ]
