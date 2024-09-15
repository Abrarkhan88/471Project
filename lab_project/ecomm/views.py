from django.shortcuts import render, get_object_or_404
from .models import Product, Reviews
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

def index(request):
    product = Product.objects.all()

    return render(request, "index.html", {"product": product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    products = Product.objects.filter(type = product.type)
    rev = Reviews.objects.filter(product = product)
    user = request.user
    
    return render(request, "product_detail.html", {"product": product, "products": products, "rev" : rev, "user" : user})

def product_from_cat(request, category):
    product = Product.objects.filter(category = category)

    if not product:
        product = Product.objects.filter(type = category)

        # return render(request, "all_prods_template.html", {"product" : product, "type": category})

    return render(request, "all_prods_template.html", {"product" : product, "category" : category})

@login_required
def reviews(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    # rev, created = Reviews.objects.get_or_create(product_id = product_id)

    if request.method == "POST":
        review_text = request.POST.get("review")

        if review_text:
            Reviews.objects.create(product_id = product_id, user = request.user, review_box = review_text)
    
    rev = Reviews.objects.filter(product = product)

    user = request.user
    

    return render(request, "product_detail.html", {"rev" : rev, "product" : product})