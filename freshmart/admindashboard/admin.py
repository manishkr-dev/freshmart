# from django.contrib import admin
# from . models import *
# # Register your models here.

# admin.site.register(Customer)
# # admin.site.unregister(Customer)

# admin.site.register(Category)


# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ('product_category',)
#     class Meta:
#         model = product
# admin.site.register(product,ProductAdmin)


# from django.contrib import admin
# from .models import product, Category, Customer

# admin.site.register(Customer)
# admin.site.register(Category)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'product_category', 'product_state', 'product_available')
#     list_filter = ('product_category', 'product_state', 'product_available')

#     class Meta:
#         model = product

# admin.site.register(product, ProductAdmin)

from django.contrib import admin
from .models import product, Customer, Category, StateChoicesTag

# Register Customer and Category models
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(StateChoicesTag)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'get_product_states', 'product_available')
    list_filter = ('product_category', 'product_state')
    search_fields = ('product_name',)  # Allow search by product name
    
    # Custom method to display the ManyToManyField 'product_state' in the admin list
    def get_product_states(self, obj):
        # Join the display names of the states associated with the product
        return ", ".join([state.get_state_display() for state in obj.product_state.all()])
    
    get_product_states.short_description = 'Product States'  # Set a label for the column

    class Meta:
        model = product

# Register Product model with the customized admin class
admin.site.register(product, ProductAdmin)

