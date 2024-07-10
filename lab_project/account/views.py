from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

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

        user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
        user.save()
        print("user created")

        return redirect('/')
    else:
        return render(request, "signup.html")

# def login(request):
#     if request.method != "POST":
#         return render(request, 'login.html')
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
    else:
        return render(request, "login.html")
    
