from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "product_img")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)