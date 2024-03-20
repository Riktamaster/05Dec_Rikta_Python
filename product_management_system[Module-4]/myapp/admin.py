from django.contrib import admin
from .models import *

# Define custom admin class for product_mst
class ProductMstAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name')  # Specify which fields to display in the list view

# Define custom admin class for product_sub_cat
class ProductSubCatAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_price', 'product_model', 'product_ram')  # Specify which fields to display in the list view
    list_filter = ['product']  # Add filters for product field

# Register your models with the custom admin classes
admin.site.register(product_mst, ProductMstAdmin)
admin.site.register(product_sub_cat, ProductSubCatAdmin)
