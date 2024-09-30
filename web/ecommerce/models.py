from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support 
from PIL import Image
from django.utils import timezone

# Create variable ENVIRONMENT for function validate interval
MIN_INT = 0
MIN_FLOAT = 0.0
MAX_RATE = 20
MIN_QUANTITY = 0
MAX_QUANTITY = 100
MAX_PRICE = 10000.0
# Default value test
DEFAULT_VALUE = 20240926

# Create Class Product :
class Product(models.Model):
	"""
	Class of product :	
		id: number; Primary key
		code: string;
		name: string;
		description: string;
		image: string;
		category: string;
		price: float; de 0.0 à 10000.0 €  
		quantity: integer; de 0 à 100
		internalReference: string;
		shellId: number;
		inventoryStatus: "INSTOCK" | "LOWSTOCK" | "OUTOFSTOCK";
		rating: integer 0 à 20;
		createdAt: Number;
		updatedAt: number;
	"""
	id = models.fields.IntegerField(primary_key=True)
	code = models.fields.CharField(max_length=10)
	name = models.fields.CharField(max_length=50)
	description = models.fields.CharField(max_length=200)
	
	image = models.ImageField(upload_to='pictures/',default='pictures/icon-152x152.png',blank=True)
	
	# Class for choice of product's category
	class Category(models.TextChoices):
		HIGH_TECH = 'High-Tech'
		SUITS = 'Suits'
		PROGRAM = 'Program'
		PC_COMPONENT = 'PC_Component'
		ACCESSORY = 'Accessories'
		OTHERS = 'Others' 
	# Recover category.choices  
	category = models.fields.CharField(choices=Category.choices, max_length=13,default='Others')
	
	# Validate interval : It must be between 0 and MAX_PRICE in float format
	def validate_interval_price(value):
		if value < MIN_FLOAT or value > MAX_PRICE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_PRICE},)          
	price = models.fields.FloatField(validators=[validate_interval_price])
	
	# Validate interval : It must be between 0 and MAX_QUANTITY in integer format
	def validate_interval_quantity(value):
		if value < MIN_QUANTITY or value > MAX_QUANTITY:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_QUANTITY},)       
	quantity = models.fields.IntegerField(validators=[validate_interval_quantity])
	
	internalReference = models.fields.CharField(max_length=13) 
	shellId = models.fields.IntegerField(default=15) 
	
	# Class Inventory 
	class Inventory (models.TextChoices):
		INSTOCK = "INSTOCK",
		LOWSTOCK = "LOWSTOCK",
		OUTOFSTOCK = "OUTOFSTOCK",
	inventoryStatus = models.fields.CharField(max_length = 10, choices=Inventory.choices)
	
	# Note between 0 and 
	def validate_interval(value):
		if value < MIN_INT or value > MAX_RATE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_RATE},)
	rating = models.fields.IntegerField(validators=[validate_interval])
	
	# Date under integer format :20211001
	createdat =  models.fields.IntegerField(default = DEFAULT_VALUE)
	# Date of update products
	updatedat = models.fields.IntegerField(default = DEFAULT_VALUE)
	
	def __str__(self):
	   return self.name
