from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    user = request.user

    cart, created = Cart.objects.get_or_create(user = user)
    cart_item, created = CartItem.objects.get_or_create(cart = cart, product = product)

    cart_item.product_name = product.name
    cart_item.product_img = product.img
    cart_item.quantity += 1
    cart_item.price += product.price
    cart_item.save()

    # return render(request, "cart.html")

    return redirect('view_cart')

@login_required
def view_cart(request):
    user = request.user
    cart = Cart.objects.get(user = user)
    cart_items = CartItem.objects.filter(cart = cart)

    return render(request, 'cart.html', {"cart_items" : cart_items})

# @login_required
# def remove_from_cart(request, product_id):
#     product = get_object_or_404(Product, id = product_id)
#     user = request.user