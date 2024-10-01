#!/usr/bin/env python3

from django.contrib import admin
from ecommerce.models import Product

# ***************
# Register  models Product for admin page
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        (None,               {'fields': ['code']}),
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['image']}),
        (None,               {'fields': ['category']}),
        (None,               {'fields': ['price']}),
        (None,               {'fields': ['quantity']}),
        (None,               {'fields': ['shellId']}),
        (None,               {'fields': ['internalReference']}),       
        (None,               {'fields': ['inventoryStatus']}),
        (None,               {'fields': ['rating']}),
        (None,               {'fields': ['createdat']}),
        (None,               {'fields': ['updatedat']}), 

    ]
    list_display = ('id','code','name', 'description','image', 'category','price',
        'quantity','internalReference','shellId','inventoryStatus','rating',
        "createdat","updatedat")

admin.site.register(Product,ProductAdmin)

