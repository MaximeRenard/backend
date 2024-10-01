#!/usr/bin/env python3
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Import Model Data base
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json

# ***************************************
# Welcome

# Welcome Test Front end  
def home_page(request):
	"""
	 METHOD GET PAGE
	 return page with basic html "Hello"
	"""
	return render(request,'ecommerce/home.html')


# ***********************************
# Ressource **/products** 
# Function Create products

# ***************
def create_a_new_product(request):
	"""

		IN : Body json in Postman
		return Save product in store

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
		# Save product in database 
		new_product.save()
		
		return HttpResponse(status=200)
	else:
		raise HttpResponseNotAllowed("Method is not supported")

# ***************
# Retrieve all products
def get_all_product(request):
	"""

		IN : Request in postman
		return  Display all product of ecommerce
		
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
# Retrieve one products id

def get_product_by_id(request, product_id):
	"""

		IN : Request in postman and id <integer> of a product in store
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
# Function update product Quantity -1 or sold
def update_product_by_id(request, product_id):
	"""

		IN : Body json with new characteristic of specific product
		OUT: Update product on database
		
	"""
	if request.method == 'PATCH':
		body = json.loads(request.body.decode('utf-8'))
		# Validate id product
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
		
		new_updateat = body.get("updatedat")    
		
		# Function to find product in store else return error 
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
# Function delete product
def delete_product_by_id(request, product_id):
	"""

		IN : Request in postman and Recover product_id in request 
		OUT: Delete product/id of ecommerce
		
	"""
	if request.method == 'DELETE':
		# Fin product ID to 
		try:
			product = Product.objects.get(pk=product_id)
		except Product.DoesNotExist:
			raise Http404("product does not exist")
        
		product.delete()
		return HttpResponse(status=200)
	else:
		raise HttpResponseNotAllowed("Method is not supported")

