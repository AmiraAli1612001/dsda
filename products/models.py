from django.db import models

# Create your models here.

class Product(models.Model):
   image = models.ImageField()
   name = models.CharField(max_length=250)
   price = models.FloatField(default=0)
   alternatePrice = models.FloatField(default=0)
   rate = models.BigIntegerField()
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   desciption = models.TextField()
   def __str__(self):
      return self.name





class SelectedProducts(models.Model):
   image = models.ImageField()
   name = models.CharField(max_length=250)
   price = models.FloatField(default=0)
   qty = models.IntegerField(default=0)
   totalPrice = models.FloatField(default=0)
   def __str__(self):
      return self.name