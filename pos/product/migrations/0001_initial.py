# Generated by Django 3.0.4 on 2020-04-14 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=16, unique=True)),
                ('customer_address', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('paid_total', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='product.Customer')),
                ('sold_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('product_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gsm', models.CharField(choices=[('25', 25), ('30', 30), ('40', 40), ('50', 50), ('60', 60), ('70', 70), ('80', 80), ('90', 90), ('100', 100), ('110', 110)], max_length=4)),
                ('bag_purchase_price', models.FloatField(default=0.0)),
                ('marketing_cost', models.FloatField(default=0.0)),
                ('transport_cost', models.FloatField(default=0.0)),
                ('printing_cost', models.FloatField(default=0.0)),
                ('vat', models.FloatField(default=0.0)),
                ('profit', models.FloatField(default=0.0)),
                ('discount_percent', models.IntegerField(default=0)),
                ('discount_min_purchase', models.IntegerField(default=0)),
                ('stock_total', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='product.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=16, unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplierTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_supplied', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant', to='product.ProductVariant')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_supplier', to='product.Supplier')),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='product.Size'),
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_history', to='product.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_product', models.FloatField(default=0.0)),
                ('discount_percent', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_item_order', to='product.Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ProductVariant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='productvariant',
            unique_together={('color', 'size', 'product', 'gsm', 'category')},
        ),
    ]
