# Generated by Django 5.1 on 2024-09-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0010_movieproxy_product_product_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieProxy',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_State',
        ),
        migrations.AddField(
            model_name='product',
            name='product_state',
            field=models.CharField(choices=[('RECENT PRODUCT', 'Recent Product'), ('FEATURED PRODUCT', 'Featured Product'), ('TRENDING PRODUCT', 'Trending Product'), ('NEW PRODUCT ARRIVALS', 'New Product Arrivals')], default='FEATURED PRODUCT', max_length=50),
        ),
    ]
