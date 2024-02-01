from django.db import models

class Buyer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Seller(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    start_date = models.DateField()
    vacancy = models.CharField(
        max_length=23,
        choices={
            "seller": "seller",
            "chef seller": "chef seller",
            "sold department manager": "sold department manager"}
    )


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    storage_amount = models.IntegerField()


class SoldInfo(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_date = models.DateField()
    sold_price = models.FloatField()
    product_amount = models.IntegerField()


