# Generated by Django 5.1 on 2024-09-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0008_product_product_priceoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_weight',
            field=models.CharField(max_length=255),
        ),
    ]
