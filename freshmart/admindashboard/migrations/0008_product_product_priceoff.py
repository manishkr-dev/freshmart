# Generated by Django 5.1 on 2024-09-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0007_category_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_priceoff',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
