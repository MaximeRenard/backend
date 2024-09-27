from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Import Model Data base
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json

# ***************************************
# Welcome page

# Welcome Page  
def home_page(request):
	"""
	  Home page
	  Methode GET
	"""
	return render(request,'ecommerce/home.html')


# Page Frontend Contact 
def contact_page(request):
	"""
	Create page contact
	Methode GET 
	"""
	# Ajouter formulaire 
	return render(request,'ecommerce/contact.html')

# ***********************************
# Ressource **/products** 
# Function Create products

# ***************
# Requst POST
def create_a_new_product(request):
	"""

		IN : Body json
		OUT: Save new product in database

	"""
	if request.method == 'POST':
		body = json.loads(request.body.decode('utf-8'))
		new_id = body.get("id")
		new_code = body.get("code")
		new_name = body.get("name")
		new_description = body.get("description")
		new_image = body.get("image")
		new_category = body.get("category")
		new_quantity = body.get("quantity")
		new_internalReference = body.get("internalReference")
		newshellId = body.get("shellId")
		new_inventoryStatus = body.get("inventoryStatus")
		new_rating = body.get("rating")
		new_price = body.get("price")
		new_createdat = body.get("createdat")
		new_updateat = body.get("updatedat")
		new_product = Product(id=new_id,code = new_code,name = new_name, description = new_description,
				image =new_image, category = new_category,quantity = new_quantity,internalReference = new_internalReference,
				shellId = newshellId,inventoryStatus = new_inventoryStatus,
				rating = new_rating,price = new_price,createdat = new_createdat,
				updatedat = new_updateat)
		# save new product in database
		new_product.save()
		
		return HttpResponse(status=200)
	else:
		raise HttpResponseNotAllowed("Method is not supported")

# ***************
# Retrieve all products : GET Method
def get_all_product(request):
	"""

		IN : Request in postman
		OUT: Display product of ecommerce
		
	"""
	if request.method == 'GET':
		query_set = Product.objects.all()
		data = serializers.serialize("json", query_set)
		return HttpResponse(data)
	else:
		raise HttpResponseNotAllowed("Method is not supported")



# ***********************************
# RESSOURCE **/products/:id**

# ***************
# Retrieve one products id : GET Method
#def get_product_id(request):
def get_product_by_id(request, product_id):
	"""

		IN : Request in postman and Recover id of product
		OUT: Display product/id of ecommerce
		
	"""
	if request.method == 'GET':
		try:
			query_set = Product.objects.filter(pk=product_id)
		except Product.DoesNotExist:
			raise Http404("Product request does not exist")
		data = serializers.serialize("json", query_set)
		return HttpResponse(data)
	else:
		raise HttpResponseNotAllowed("Method is not supported")


# ***************
# Function update product Quantity or stock after purchase or sold
def update_product_by_id(request, product_id):
	"""

		IN : Body json with chage of product
		OUT: Update product on database
		
	"""
	if request.method == 'PATCH':
		body = json.loads(request.body.decode('utf-8'))
		new_id = body.get("id")
		new_code = body.get("code")
		new_name = body.get("name")
		new_description = body.get("description")
		new_image = body.get("image")
		new_category = body.get("category")
		new_quantity = body.get("quantity")
		new_internalReference = body.get("internalReference")
		new_shellId = body.get("shellId")
		new_inventoryStatus = body.get("inventoryStatus")
		new_rating = body.get("rating")
		new_price = body.get("price")
		# Update no change createat
		# new_createdat = body.get("createdat")
		new_updateat = body.get("updatedat")    
		try:
			product = Product.objects.get(pk=product_id)
		except Product.DoesNotExist:
  			raise Http404("product does not exist") 

        # No change of id       
		product.code = new_code
		product.name = new_name
		product.description = new_description
		product.image = new_image
		product.category = new_category
		product.quantity = new_quantity
		product.internalReference = new_internalReference
		product.shellId = new_shellId
		product.inventoryStatus = new_inventoryStatus
		product.rating  = new_rating
		product.price = new_price
		# No change of createat
		product.updatedat = new_updateat
		product.save()             
		return HttpResponse(status=200)    
	else:
		raise HttpResponseNotAllowed("Method is not supported")


# ***************
# Function delete product : DELETE Method
def delete_product_by_id(request, product_id):
	"""

		IN : Request in postman and Recover id of product
		OUT: Delete product/id of ecommerce
		
	"""
	if request.method == 'DELETE':
		try:
			product = Product.objects.get(pk=product_id)
		except Product.DoesNotExist:
			raise Http404("product does not exist")
        
		product.delete()
		return HttpResponse(status=200)
	else:
		raise HttpResponseNotAllowed("Method is not supported")

