# Generated by Django 3.0.7 on 2020-10-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201001_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('OutForDelivery', 'OutForDelivery'), ('OutOfStock', 'OutOfStock'), ('Not Available', 'Not Available')], max_length=100, null=True),
        ),
    ]
