# Generated by Django 5.1 on 2024-08-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0003_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
