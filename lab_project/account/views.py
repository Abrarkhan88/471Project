from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
# from .backends import EmailBackend
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username is already taken.")
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email is already taken.")
                return redirect('signup')
            else:
                verf_link = str(uuid.uuid4())
                user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, mobile_no = mobile_no, password = password, verf_link = verf_link)
                user.save()

                send_email(email, verf_link)
                
                return redirect('verify_account')
        else:
            messages.info(request, "Passwords do not match.")
            return redirect('signup')
        
    else:
        return render(request, "signup.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid email and password")
            return redirect("login")
    else:
        return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/")

def link_send(request):
    return render(request, 'verify_account.html')

def send_email(email, link):
    sub = "Please Verify | CSE471 Lab Project Summer 2024"
    msg = f"Please click on the link to verify your account http://127.0.0.1:8000/account/verify/{link}"
    email_from = settings.EMAIL_HOST_USER
    email_to = [email]
    send_mail(sub, msg, email_from, email_to)

def verify(request, verf_link):
    user = User.objects.filter(verf_link = verf_link).first()

    if user:
        if user.email_verified == True:
            messages.info(request, "Your account is already verified")
            return render(request, "login.html")
        else:
            user.email_verified = True
            user.save()
            # messages.success(request, "Congratulations! Your account has been verified.")

        return render(request, "verified.html")
    else:
        return render(request, "verf_error.html")

def password_reset(request):
    return render(request, "resetPassword/passresetmail.html")

def my_profile(request):
    pass
