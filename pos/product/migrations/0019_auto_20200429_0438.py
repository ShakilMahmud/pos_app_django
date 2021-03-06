# Generated by Django 3.0.4 on 2020-04-28 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20200428_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderedItem_variants', to='product.ProductVariant'),
        ),
        migrations.AlterField(
            model_name='suppliertransaction',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_variant', to='product.ProductVariant'),
        ),
    ]
