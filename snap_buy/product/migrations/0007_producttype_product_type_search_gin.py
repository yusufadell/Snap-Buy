# Generated by Django 5.0.8 on 2024-08-09 17:47

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_product_product_search_gin_product_product_tsearch_and_more"),
        ("tax", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="producttype",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name", "slug"],
                name="product_type_search_gin",
                opclasses=["gin_trgm_ops", "gin_trgm_ops"],
            ),
        ),
    ]
