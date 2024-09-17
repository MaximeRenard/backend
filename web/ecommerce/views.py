from django.shortcuts import render
from django.http import HttpResponse

# Import Model Data base
from ecommerce.models import Product

# Page Accueil to test postman
def home_page(request):
	"""
	 METHOD GET PAGE
	"""
	return render(request,'ecommerce/home.html')


# Page Frontend to test with Postman 
def contact_page(request):
	"""
	Create page contact avec formulaire
	Return validation envoi
	"""
	# Ajouter formulaire 
	return render(request,'ecommerce/contact.html')


# Objectif 1 Backend Retrieve all of Products
def listing_products(request):
	"""
		Create Page listing des produits
		Return List of products 
	"""
	products = Product.objects.all()
	# Ajouter Produits et lecture des produits sous un format liste
	return render(request,'ecommerce/product.html', {'products': products})
	

# Retrieve one products id
#def get_product_id(request):

# Function update product Quantite -1
#def update_product_id(request):

# Function delete products
#def delete_product_id(request):

# Function Create products
#def create_products(request):
# in admin.py
# python3 manage.py shell