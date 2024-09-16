from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support 
# Create variable ENVIRONMENT
MIN_INT = 0
MIN_FLOAT = 0.0
MAX_RATE = 10.0
MAX_QUANTITY = 100
MAX_PRICE = 10000.0



# Create of class of products.
class Products(models.Model):
	"""
	Class Products :
	  id: number;
	  code: string;
	  name: string;
	  description: string;
	  image: string;
	  category: string;
	  price: number;
	  quantity: number;
	  internalReference: string;
	  shellId: number;
	  inventoryStatus: "INSTOCK" | "LOWSTOCK" | "OUTOFSTOCK";
	  rating: number;
	  createdAt: number;
	  updatedAt: number;
	"""
	id = models.fields.IntegerField(primary_key=True)
	code = models.fields.CharField(max_length=10)
	name = models.fields.CharField(max_length=50)
	description = models.fields.CharField(max_length=200)
	
	#image = in db
	
	class Category(models.TextChoices):
		HIGH_TECH = 'High-Tech'
		SUITS = 'Suits'
		PROGRAM = 'Program'
		PC_COMPONENT = 'Portable'
		OTHERS = 'Others'
	category = models.fields.CharField(choices=Category.choices, max_length=9,default='Others')
	def validate_interval_price(value):
		if value < MIN_FLOAT or value > MAX_PRICE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_PRICE},)		
	price = models.fields.FloatField(validators=[validate_interval_price])# euros
	def validate_interval_quantity(value):
		if value < MIN_INT or value > MAX_QUANTITY:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_QUANTITY},)		
	
	quantity = models.fields.IntegerField(validators=[validate_interval_quantity])#validation 
	
	#internalReference = models.fields.IntegerField() # definir
	#shellId = models.fields.IntegerField() # definir
	
	INVENTORY = {
		"I": "INSTOCK",
		"L": "LOWSTOCK",
		"O": "OUTOFSTOCK",
	}
	inventoryStatus = models.fields.CharField(max_length = 1, choices=INVENTORY)
	def validate_interval(value):
		if value < MIN_FLOAT or value > MAX_RATE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_RATE},)
	rating = models.fields.FloatField(validators=[validate_interval])# Note between 0 and 10
	
	#createdAt =
	#updateAt = 

