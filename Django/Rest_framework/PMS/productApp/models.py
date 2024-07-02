from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=30)
    p_price = models.FloatField()

    def __str__(self): 
        return self.p_name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
