from django.shortcuts import render
from django.http import HttpResponse

# Import Model Data base
from ecommerce.models import Products

# Fonction test 
def home_page(request):
    return render(request,'ecommerce/home.html')



# Objectif 1 Front end
def listing_products(request):
	"""
		Create Page listing des produits
		Return List of products 
	"""
	products = Products.objects.all()
	# Ajouter Produits et lecture des produits sous un format liste
	return render(request,'ecommerce/product.html', {'products': products})
	
# Objectif 2 Frontend
def contact_page(request):
	"""
	Create page contact avec formulaire
	Return validation envoi
	"""
	# Ajouter formulaire 
	return HttpResponse('<h1>Page Contact</h1>')

