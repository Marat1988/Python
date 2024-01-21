from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    site = models.CharField(max_length=25)
    telephone = models.CharField(max_length=20)
