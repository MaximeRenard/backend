# Generated by Django 4.2.11 on 2024-09-19 16:26

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
                (
                    "image",
                    models.ImageField(
                        default="pictures/icon-152x152.png", upload_to="pictures/"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("High-Tech", "High Tech"),
                            ("Suits", "Suits"),
                            ("Program", "Program"),
                            ("Portable", "Pc Component"),
                            ("Accessories", "Accessory"),
                            ("Others", "Others"),
                        ],
                        default="Others",
                        max_length=13,
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[ecommerce.models.Product.validate_interval_price]
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[ecommerce.models.Product.validate_interval_quantity]
                    ),
                ),
                ("internalReference", models.CharField(max_length=13)),
                ("shellId", models.IntegerField(default=15)),
                (
                    "inventoryStatus",
                    models.CharField(
                        choices=[
                            ("INSTOCK", "Instock"),
                            ("LOWSTOCK", "Lowstock"),
                            ("OUTOFSTOCK", "Outofstock"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        validators=[ecommerce.models.Product.validate_interval]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=100)),
                ("latitude", models.FloatField(default=0)),
                ("longitude", models.FloatField(default=0)),
            ],
        ),
    ]
