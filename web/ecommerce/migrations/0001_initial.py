# Generated by Django 5.1.1 on 2024-09-16 09:20

import ecommerce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('High-Tech', 'High Tech'), ('Suits', 'Suits'), ('Program', 'Program'), ('Portable', 'Pc Component'), ('Others', 'Others')], default='Others', max_length=9)),
                ('price', models.FloatField(validators=[ecommerce.models.Products.validate_interval_price])),
                ('quantity', models.IntegerField(validators=[ecommerce.models.Products.validate_interval_quantity])),
                ('inventoryStatus', models.CharField(choices=[('I', 'INSTOCK'), ('L', 'LOWSTOCK'), ('O', 'OUTOFSTOCK')], max_length=1)),
                ('rating', models.FloatField(validators=[ecommerce.models.Products.validate_interval])),
            ],
        ),
    ]
