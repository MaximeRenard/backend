from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Import Model Data base
from ecommerce.models import Product
import json

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
	# <ul>
    #            {% for product in products %}
    #            <li>
    #                {{ product.id }}
    #                {{ product.name }}
    #            </li>
    #            {% endfor %}
    #        </ul>
	# Ajouter Produits et lecture des produits sous un format liste
	return render(request,'ecommerce/product.html')
	
"""
def get_all_restaurants(request):
    query_set = Restaurant.objects.all()
    data = serializers.serialize("json", query_set)
    return HttpResponse(data)
# Retrieve one products id
#def get_product_id(request):
def get_restaurant_by_id(request, restaurant_id):
    try:
        query_set = Restaurant.objects.filter(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
        data = serializers.serialize("json", query_set)
    return HttpResponse(data)
# Function update product Quantite -1
#def update_product_id(request):
def update_restaurant_by_id(request, restaurant_id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        new_name = body.get("name")
        new_address = body.get("address")
        new_latitude = body.get("latitude")
        new_longitude = body.get("longitude")        try:
            tag = Tag.objects.get(pk=body.get("tag_id"))
        except Tag.DoesNotExist:
            raise Http404("Tag does not exist")        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404("Restaurant does not exist")        restaurant.name = new_name
        restaurant.address = new_address
        restaurant.latitude = new_latitude
        restaurant.longitude = new_longitude
        restaurant.save()        tag.restaurants.add(restaurant)
        tag.save()        return HttpResponse(status=200)    else:
        raise HttpResponseNotAllowed("Method is not supported")
# Function delete products
#def delete_product_id(request):
def delete_restaurant_by_id(request, restaurant_id):
    if request.method == 'DELETE':
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404("Restaurant does not exist")
        
        restaurant.delete()
        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")


"""

# Function Create products
"""
def create_a_new_restaurant(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        new_name = body.get("name")
        new_address = body.get("address")
        new_latitude = body.get("latitude")
        new_longitude = body.get("longitude")
        try:
             tag = Tag.objects.get(pk=body.get("tag_id"))
        except Tag.DoesNotExist:
             raise Http404("Tag does not exist")
        new_restaurant = Restaurant(name=new_name,        address=new_address, latitude=new_latitude, longitude=new_longitude)
        new_restaurant.save()
        tag.restaurants.add(new_restaurant)
        tag.save()
        return HttpResponse(status=200)
     else:
        raise HttpResponseNotAllowed("Method is not supported")
"""
def create_product(request):
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
		try:
			tag = Tag.objects.get(pk=body.get("tag_id"))
		except Tag.DoesNotExist:
			raise Http404("Tag does not exist")
		new_product = Product(id=new_id,code = new_code,name = new_name, description = new_description,new =new_image, category = new_category,price = new_price,quantity = new_quantity,internalReference = new_internalReference,shellId = newshellId,inventoryStatus = new_inventoryStatus,rating = new_rating)
		new_product.save()
		tag.new_product.add(new_product)
		tag.save()
		return HttpResponse(status=200)
	else:
		raise HttpResponseNotAllowed("Method is not supported")

