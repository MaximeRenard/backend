from django.urls import path
from . import views

# ***************
# Url pattern for application ecommerce
urlpatterns = [
    path('ecommerce/new/', views.create_a_new_product, name='create a new product in store'),    
    path('ecommerce/', views.get_all_product, name='get all product of store'),    
    path('ecommerce/<int:product_id>/', views.get_product_by_id, name='get a specific product'),    
    path('ecommerce/patch/<int:product_id>/', views.update_product_by_id, name='update a product of store'),    
    path('ecommerce/delete/<int:product_id>/', views.delete_product_by_id, name='delete a product of store'),
]
