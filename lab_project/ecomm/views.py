from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    product = Product.objects.all()

    return render(request, "index.html", {"product": product})