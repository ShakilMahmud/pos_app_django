# Generated by Django 3.0.4 on 2020-04-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200419_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
