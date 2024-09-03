from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('signup', views.signup, name = "signup"),
    path('login', views.user_login, name = "login"),
    path('logout', views.user_logout, name = "logout"),
    # path('verify_account', views.link_send, name = 'verify_account'),
    path('link_send/', views.link_send, name='link_send'),
    path('verify/<verf_link>', views.verify, name="verify"),
    # path('verified', views.)
    path('verf_error', views.verf_error, name = "verf_error"),
    path("reset_password/",auth_views.PasswordResetViews.as_views(†emplate_name=templates/passresetmail.html),name="Reset_password"),
    path("reset_password_sent/",auth_views.PasswordResetDoneViews.as_views(template_name=account/templates/passresetsent.html),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmViews.as_views(template_name=account/templates/passresetform.html),name="password_reset_confirm"),
    path("reset_password_complete/",auth_views.PasswordResetCompleteViews.as_views(template_name=/account/templates/passresetdone.html),name="password_reset_complete"),

]
