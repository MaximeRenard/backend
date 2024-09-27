from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support 
from PIL import Image
from django.utils import timezone

# Create variable ENVIRONMENT
MIN_INT = 0
MIN_FLOAT = 0.0
MAX_RATE = 20
MAX_QUANTITY = 0
MAX_QUANTITY = 100
MAX_PRICE = 10000.0
# Default value test
DEFAULT_VALUE = 20240926

# Create Class Product :
class Product(models.Model):
	"""
		id: number; Primary key
		code: string;
		name: string;
		description: string;
		image: string;
		category: string;
		price: number; de 1.0 à 100000 
		quantity: number; de 0 à 100
		internalReference: string;
		shellId: number;
		inventoryStatus: "INSTOCK" | "LOWSTOCK" | "OUTOFSTOCK";
		rating: note de 1 à 20;
		createdAt: Number;
		updatedAt: number;
	"""
	id = models.fields.IntegerField(primary_key=True)
	code = models.fields.CharField(max_length=10)
	name = models.fields.CharField(max_length=50)
	description = models.fields.CharField(max_length=200)
	
	image = models.ImageField(upload_to='pictures/',default='pictures/icon-152x152.png',blank=True)
	
	class Category(models.TextChoices):
		HIGH_TECH = 'High-Tech'
		SUITS = 'Suits'
		PROGRAM = 'Program'
		PC_COMPONENT = 'Portable'
		ACCESSORY = 'Accessories'
		OTHERS = 'Others'   
	category = models.fields.CharField(choices=Category.choices, max_length=13,default='Others')
	
	def validate_interval_price(value):
		if value < MIN_FLOAT or value > MAX_PRICE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_PRICE},)          
	price = models.fields.FloatField(validators=[validate_interval_price])
	
	def validate_interval_quantity(value):
		if value < MIN_QUANTITY or value > MAX_QUANTITY:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_QUANTITY},)       
	quantity = models.fields.IntegerField(validators=[validate_interval_quantity])
	
	internalReference = models.fields.CharField(max_length=13) 
	shellId = models.fields.IntegerField(default=15) 
	
	class Inventory (models.TextChoices):
		INSTOCK = "INSTOCK",
		LOWSTOCK = "LOWSTOCK",
		OUTOFSTOCK = "OUTOFSTOCK",
	inventoryStatus = models.fields.CharField(max_length = 10, choices=Inventory.choices)
	
	def validate_interval(value):
		if value < MIN_INT or value > MAX_RATE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_RATE},)
	rating = models.fields.IntegerField(validators=[validate_interval])
	
	# Date sous format integer
	createdat =  models.fields.IntegerField(default = DEFAULT_VALUE)
	# Date of update products
	updatedat = models.fields.IntegerField(default = DEFAULT_VALUE)
	
	def __str__(self):
	   return self.name
