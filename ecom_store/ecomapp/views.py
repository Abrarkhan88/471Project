from django.shortcuts import render
from .models import Shop

# Create your views here.
def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'ecomapp/login.html')

def signup_view(request):
    return render(request, 'ecomapp/signup.html')
