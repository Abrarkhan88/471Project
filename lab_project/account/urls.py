from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('login', views.user_login, name = "login"),
    path('logout', views.user_logout, name = "logout"),
    # path('verify_account', views.link_send, name = 'verify_account'),
    path('link_send/', views.link_send, name='link_send'),
    path('verify/<verf_link>', views.verify, name="verify"),
    # path('verified', views.)
    path('verf_error', views.verf_error, name = "verf_error")
]