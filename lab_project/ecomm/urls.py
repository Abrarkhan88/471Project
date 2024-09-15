from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
<<<<<<< Updated upstream
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_category/<str:category>/', views.product_from_cat, name = "product_from_cat")
=======
    path('product/<int:product_id>/', views.product_detail, name='product_detail')
>>>>>>> Stashed changes
]