# Generated by Django 4.2.2 on 2023-07-09 22:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="product",
            index_together=set(),
        ),
    ]
