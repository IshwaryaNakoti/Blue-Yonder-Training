from django.db import models

# Create your models here.
class Product(models.Model):
    p_id =  models.IntegerField()
    p_name = models.CharField(max_length=30)
    p_price = models.FloatField()
