from django.db import models

# Create your models here.

class Employee(models.Model):
    empName = models.CharField(max_length=30)
    empNo = models.IntegerField()
    empSal = models.FloatField()
    empAddress = models.CharField(max_length=50)

