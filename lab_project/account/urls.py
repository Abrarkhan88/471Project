from django.urls import path
from . import views
from .views import password_reset,verify_OTP

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('login', views.user_login, name = "login"),
    path('logout', views.user_logout, name = "logout"),
    path('verify_account', views.link_send, name = 'verify_account'),
    path('verify/<verf_link>', views.verify, name = "verify"),
    path('password_reset', views.password_reset, name = 'password_reset'),
    path('my_profile', views.my_profile, name = 'my_profile'), 
    path('update_profile', views.updateProfile, name = "update_profile"),
<<<<<<< HEAD
    path('password_reset',views.password_reset,name="password_reset"),
    path('verify_OTP/<int:id>',views.verify_OTP,name="verify_OTP"),
=======
<<<<<<< Updated upstream
>>>>>>> cf69988f47f338691d4494be280f86cd78ecfac2
    # path('user=<int:user_id>', views.user_login, name = 'login')
=======
>>>>>>> Stashed changes
]