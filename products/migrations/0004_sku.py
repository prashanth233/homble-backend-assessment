# Generated by Django 3.2.24 on 2024-02-17 20:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240217_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('measurement_unit', models.CharField(choices=[('gm', 'Grams'), ('kg', 'Kilograms'), ('mL', 'Milliliters'), ('L', 'Liters'), ('pc', 'Piece')], default='gm', max_length=2)),
                ('price', models.PositiveIntegerField()),
                ('platform_commission', models.PositiveSmallIntegerField()),
                ('cost_price', models.PositiveIntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Pending for approval'), (1, 'Approved'), (2, 'Discontinued')], default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skus', to='products.product')),
            ],
            options={
                'verbose_name': 'SKU',
                'verbose_name_plural': 'SKUs',
                'db_table': 'sku',
                'ordering': [],
            },
        ),
    ]
