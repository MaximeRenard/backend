# Generated by Django 4.2.11 on 2024-09-19 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0003_alter_product_createdat_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="createdAt",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
