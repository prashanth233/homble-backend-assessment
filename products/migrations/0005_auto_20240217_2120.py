# Generated by Django 3.2.24 on 2024-02-17 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_sku'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='selling_price',
        ),
        migrations.RenameField(
            model_name='sku',
            old_name='price',
            new_name='selling_price',
        ),
    ]