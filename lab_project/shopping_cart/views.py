from django.shortcuts import render, get_object_or_404
# from .models import Product

# Create your views here.

def view_cart(request):
    return render(request, "cart.html")

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id = product_id)

#     prod_exist = 