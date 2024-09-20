# Generated by Django 4.2.11 on 2024-09-19 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0002_product_createdat_product_updateat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="createdAt",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 9, 19, 16, 45, 9, 8245)
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, default="pictures/icon-152x152.png", upload_to="pictures/"
            ),
        ),
    ]
