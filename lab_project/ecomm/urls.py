from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/type/<str:type>/', views.products_by_type, name='products_by_type'),
]