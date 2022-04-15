from django.db import models

# Create your models here.
class Product_Database(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    product_name=models.CharField(max_length=70)
    price=models.IntegerField()
    link=models.CharField(max_length=70)


class dummy(models.Model):
    des=models.CharField(max_length=70)
    imag_url=models.CharField(max_length=512)
    linkA=models.CharField(max_length=1070)
    linkF=models.CharField(max_length=1070)
    linkC=models.CharField(max_length=1070)
    amazonP=models.IntegerField()
    flipkartP=models.IntegerField()
    cromaP=models.IntegerField()

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	password = models.CharField(max_length=100)


class Category(models.Model):
	category_name = models.CharField(max_length=50)
	

class Product(models.Model):
    product_name = models.CharField(max_length=70)
    category_name = models.CharField(max_length=70)
    product_price = models.IntegerField()
    product_link = models.CharField(max_length=70)



