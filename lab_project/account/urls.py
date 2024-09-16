from django.urls import path
from . import views
<<<<<<< HEAD
from .views import password_reset,verify_OTP
=======
from django.contrib.auth import views as auth_views
>>>>>>> 511e21415ebfe7a1b08d70a09452f2bb53d043ab

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('login', views.user_login, name = "login"),
    path('logout', views.user_logout, name = "logout"),
    path('verify_account', views.link_send, name = 'verify_account'),
    path('verify/<verf_link>', views.verify, name = "verify"),
    path('password_reset', views.password_reset, name = 'password_reset'),
<<<<<<< HEAD
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
=======
    path('my_profile', views.my_profile, name = 'my_profile'),

    #password recovery 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword/passresetmail.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='resetPassword/passresetsent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetPassword/passresetform.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPassword/passresetdone.html'), name='password_reset_complete'),

>>>>>>> 511e21415ebfe7a1b08d70a09452f2bb53d043ab
]