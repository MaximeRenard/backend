from django.contrib import admin
from django.urls import include,path
# Import des vues de django
from ecommerce import views

# Include path of project : Test of function in ecommerce/views.py with Postman 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ecommerce.urls')),
    path('home/', views.home_page,name="home_page"),
    path('contact/', views.contact_page,name="contact"),
]
