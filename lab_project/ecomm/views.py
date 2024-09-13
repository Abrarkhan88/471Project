from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def index(request):
    product = Product.objects.all()

    return render(request, "index.html", {"product": product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    products = Product.objects.filter(type = product.type)
    
    return render(request, "product_detail.html", {"product": product, "products": products})

def products_by_type(request, type):
    type = type.replace('-', ' ')
    print(type)
    products = Product.objects.filter(type=type) 
    print(products)
    return render(request, 'products_by_type.html', {'products': products, 'type': type})
