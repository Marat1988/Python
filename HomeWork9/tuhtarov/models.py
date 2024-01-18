from django.db import models


# Create your models here.

class Order(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    monthCount = models.IntegerField()
    capacity = models.IntegerField()
