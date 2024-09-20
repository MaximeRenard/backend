from django.contrib import admin
from django.urls import include,path
# Import des vues de django
from ecommerce import views
"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('ecommerce.urls')),
    path('home/', views.home_page,name="home_page"),
    path('contact/', views.contact_page,name="contact"),
    path('products/', views.listing_products,name='get_all_products'),
    #path('products/<int:product_id>/',views.products_id,name='get_product_id'),
    #path('products/update/<int:product_id>/',views.update_product,name='update_product_id'),
    #path('products/delete//<int:product_id>/',views.delete_product,name='delete_product_id'),
    path('products/patch/',views.create_product,name='create_product'),
]