from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        #mobileno = request.POST['mobileno']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username = username).exists():
                print("Username already taken.")
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                print("Email is already in use.")
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
                user.save()
                print("user created")
                
                return redirect('/')
        else:
            print("Passwords not matching")
            return redirect('signup')
        
    else:
        return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            print("Login Sucessfull")
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            #return redirect("login")
            return render(request, "signup.html")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")