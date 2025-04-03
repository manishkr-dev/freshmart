from django.db import models

# Create your models here.

class Category(models.Model):
    genre = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.genre

class Customer(models.Model):
    name=models.CharField(max_length=255)
    # we can also use this function default = user
    # name=models.CharField(max_length=255, default='user')
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    # img=models.ImageField(max_length=255)
    mobile=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    added_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.username
    
from django.db import models

# Category Model
class Category(models.Model):
    genre = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.genre


# StateChoicesTag Model
class StateChoicesTag(models.Model):
    state = models.CharField(max_length=50, choices=[
        ('RECENT PRODUCT', 'Recent Product'),
        ('FEATURED PRODUCT', 'Featured Product'),
        ('TRENDING PRODUCT', 'Trending Product'),
        ('NEW PRODUCT ARRIVALS', 'New Product Arrivals'),
    ], unique=True)

    def __str__(self):
        return self.get_state_display()


# Product Model
class product(models.Model):
    class ProductChoices(models.TextChoices):
        INSTOCK = 'IN STOCK', 'IN STOCK'
        OUTOFSTOCK = 'OUT OF STOCK', 'OUT OF STOCK'

    class StateChoices(models.TextChoices):
        RECENT_PRODUCT = 'RECENT PRODUCT', 'Recent Product'
        FEATURED_PRODUCT = 'FEATURED PRODUCT', 'Featured Product'
        TRENDING_PRODUCT = 'TRENDING PRODUCT', 'Trending Product'
        NEW_PRODUCT_ARRIVALS = 'NEW PRODUCT ARRIVALS', 'New Product Arrivals'

    # Product fields
    product_name = models.CharField(max_length=255)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_state = models.ManyToManyField(StateChoicesTag, blank=True)
    product_img = models.ImageField(null=True, blank=True, upload_to="product_img/")
    product_weight = models.CharField(max_length=255)
    product_available = models.CharField(max_length=255, choices=ProductChoices.choices, default=ProductChoices.INSTOCK)
    product_qty = models.IntegerField()
    product_orginalprice = models.IntegerField(null=True, blank=True)
    product_discountprice = models.IntegerField(null=True, blank=True)
    product_priceoff = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    # Save method to calculate discount and update availability status
    def save(self, *args, **kwargs):
        # Calculate discount percentage if original and discount prices are set and valid
        if self.product_orginalprice and self.product_discountprice:
            if self.product_discountprice < self.product_orginalprice:
                discount_value = self.product_orginalprice - self.product_discountprice
                self.product_priceoff = int((discount_value / self.product_orginalprice) * 100)
            else:
                self.product_priceoff = 0  # Ensure no negative values
        else:
            self.product_priceoff = None

        # Update stock status based on product quantity
        if self.product_qty < 1:
            self.product_available = self.ProductChoices.OUTOFSTOCK
        else:
            self.product_available = self.ProductChoices.INSTOCK

        # Save the instance
        super().save(*args, **kwargs)













