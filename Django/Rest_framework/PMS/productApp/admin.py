from django.contrib import admin
from productApp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin): 
	list_display=['p_id','p_name','p_price'] 

admin.site.register(Product)