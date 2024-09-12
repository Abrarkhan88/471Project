# shopping_cart/models.py
from django.db import models
from ecomm.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem', related_name='carts')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def save(self, *args, **kwargs):
        # Set the name field to the product's name
        self.name = self.product.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Cart {self.cart.id}"
