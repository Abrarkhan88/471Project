from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('add-to-cart/<int:product_id>', views.add_to_cart, name = "add_to_cart"), 
    path('view_cart', views.view_cart, name = "view_cart"),
    path('update_cart/<int:item_id>', views.update_cart, name = "update_cart"),
    path('download_invoice/', views.download_invoice, name='download_invoice'),
=======
    path('view_cart', views.view_cart, name = "view_cart")
>>>>>>> Stashed changes
]