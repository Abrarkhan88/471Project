from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('login', views.user_login, name = "login"),
    path('logout', views.user_logout, name = "logout"),
    path('verify_account', views.link_send, name = 'verify_account'),
    path('verify/<verf_link>', views.verify, name = "verify"),
    path('password_reset', views.password_reset, name = 'password_reset'),
    path('my_profile', views.my_profile, name = 'my_profile'),

    #password recovery 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword/passresetmail.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='resetPassword/passresetsent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetPassword/passresetform.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPassword/passresetdone.html'), name='password_reset_complete'),

]