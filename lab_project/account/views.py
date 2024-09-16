from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse



from django.contrib.auth.models import User
from .models import profile




from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
import random
from django.core.exceptions import MultipleObjectsReturned
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
            if User.objects.filter(email = email).exists():
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
    if request.method == 'POST':
        email = request.POST['email']
        OTP_token = random.randint(111111, 999999)
        try:
            user = User.objects.get(email=email)
            # prof=profile.objects.get(user=user)
            # prof.otp=OTP_token
            mail_verify_otp(user.email, OTP_token)
            return redirect('verify_OTP',id=user.id)
        except MultipleObjectsReturned:
            users = User.objects.filter(email=email)
            user = users.first()  # or handle multiple users as needed
            mail_verify_otp(user.email, OTP_token)
            messages.warning(request, "Multiple accounts found with this email. OTP sent to the first account.")
            return redirect('verify_OTP',id=user.id)
        except User.DoesNotExist:
            messages.warning(request, "Invalid email.")
    return render(request, "pass_reset.html")





# def password_reset(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         OTP_token = random.randint(111111, 999999)
#         try:
#             user = User.objects.get(email=email)
#             try:
#                 prof = Profile.objects.get(user=user)
#                 prof.otp = OTP_token
#                 prof.save()
#                 mail_verify_otp(user.email, OTP_token)
#                 return redirect('verify_OTP', id=user.id)
#             except Profile.DoesNotExist:
#                 messages.warning(request, "Profile does not exist for this user.")
#         except User.DoesNotExist:
#             messages.warning(request, "Invalid email.")
#         except MultipleObjectsReturned:
#             users = User.objects.filter(email=email)
#             user = users.first()  # or handle multiple users as needed
#             mail_verify_otp(user.email, OTP_token)
#             messages.warning(request, "Multiple accounts found with this email. OTP sent to the first account.")
#     return render(request, "pass_reset.html")



   


def mail_verify_otp(email,OTP_token):
    subject="OTP verification for password reset"
    message=f'Your OTP is : {OTP_token}'  
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject, message, from_email, recipient_list)



# def verify_OTP(request,id):
#     ser=User.objects.get(id=id)

#     context={'user':User}
#     if request.method == 'POST':
#         otp=request.POST['otp']
#         new_password=request.post['new_password']
#         # proof = profile.objects.get(user=user)
#         if proof.otp==otp:
#             user.set_password(new_password)
#             user.save()
#             messages.success(request,'Password reset done')
#             return redirect(user_login)
#         else:

#             messages.warning(request,'Invalid OTP.Please try again')



#     return render(request, "verifyOTP.html",context)



def verify_OTP(request, id):
    user = User.objects.get(id=id)  # Correctly assign the user variable

    context = {'user': user}  # Use the user variable in the context
    if request.method == 'POST':
        otp = request.POST.get('otp')
        new_password = request.POST['new_password']  # Correct the POST method

        try:
            proof = profile.objects.get(user=user)  # Check if profile exists
            if proof.otp == otp:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password reset done')
                return redirect(user_login)
            else:
                messages.warning(request, 'Invalid OTP. Please try again.')
        except profile.DoesNotExist:
            messages.warning(request, 'Profile does not exist for this user.Please signup.')
            return redirect(signup)

    return render(request, "verifyOTP.html", context)


def my_profile(request):
    pass



def updateProfile(request):
    if request.method == "POST":
        user = User.objects.get(username = request.user.username)
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
    else:
        return render(request, "update_profile.html")