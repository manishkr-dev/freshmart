# Generated by Django 5.1 on 2024-08-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0005_alter_product_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AddField(
            model_name='product',
            name='product_discountprice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_orginalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
