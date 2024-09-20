from django.contrib import admin
from ecommerce.models import Product
from .models import Restaurant
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

    ]
    list_display = ('id','code','name', 'description','image', 'category','price','quantity','internalReference','shellId','inventoryStatus','rating')
admin.site.register(Product,ProductAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['address']}),
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']})
    ]
    list_display = ('name', 'address', 'latitude', 'longitude')
admin.site.register(Restaurant, RestaurantAdmin)