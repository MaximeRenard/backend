from django.contrib import admin
from .models import Product

# Register  models Product for admin page
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        (None,               {'fields': ['code']}),
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['category']}),
        (None,               {'fields': ['price']}),
        (None,               {'fields': ['quantity']}),
        (None,               {'fields': ['internalReference']}),
        (None,               {'fields': ['inventoryStatus']}),
        (None,               {'fields': ['rating']}),

    ]
    list_display = ('code','name', 'description', 'image', 'category','price','quantity','internalReference','shellId','inventoryStatus','rating')
admin.site.register(Product,ProductAdmin)
