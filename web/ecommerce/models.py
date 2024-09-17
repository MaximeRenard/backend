from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # use if you support 
from PIL import Image
# Create variable ENVIRONMENT
# Create variable ENVIRONMENT
MIN_INT = 0
MIN_FLOAT = 0.0
MAX_RATE = 20.0
MAX_QUANTITY = 100
MAX_PRICE = 10000.0


# Create of class of products.
class Product(models.Model):
	"""
	 Create Class Product :
	  id: number; Primary key
	  code: string;
	  name: string;
	  description: string;
	  image: string;
	  category: string;
	  price: number; de 1.0 à 100000 e
	  quantity: number; de 0 à 100
	  internalReference: string;
	  shellId: number;
	  inventoryStatus: "INSTOCK" | "LOWSTOCK" | "OUTOFSTOCK";
	  rating: note de 1 à 20;
	  createdAt: date;
	  updatedAt: date;
	"""
	id = models.fields.IntegerField(primary_key=True)
	code = models.fields.CharField(max_length=10)
	name = models.fields.CharField(max_length=50)
	description = models.fields.CharField(max_length=200)
	
	image = models.ImageField(upload_to='pictures/',
        default='pictures/icon-152x152.png',
        blank=True
    )
	
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
	price = models.fields.FloatField(validators=[validate_interval_price])# euros
	def validate_interval_quantity(value):
		if value < 1.0 or value > MAX_QUANTITY:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_QUANTITY},)		
	quantity = models.fields.IntegerField(validators=[validate_interval_quantity])#validation 
	
	internalReference = models.fields.CharField(max_length=13) 
	shellId = models.fields.IntegerField(default=15) 
	
	INVENTORY = {
		"I": "INSTOCK",
		"L": "LOWSTOCK",
		"O": "OUTOFSTOCK",
	}
	inventoryStatus = models.fields.CharField(max_length = 1, choices=INVENTORY)
	def validate_interval(value):
		if value < MIN_FLOAT or value > MAX_RATE:
			raise ValidationError(_('%(value)s must be in the range [%(Min),%(Max)]'), params={'value': value,'Min' :MIN_FLOAT,'Max' :MAX_RATE},)
	rating = models.fields.FloatField(validators=[validate_interval])
	createdAt = models.fields.DateTimeField(auto_now_add=True)
	updateAt = models.fields.DateTimeField(auto_now=True)