from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request,"login_sys/index.html")

def signup(request):
    if request.method == "POST":
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pass"]
        password2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        if password != password2:
            messages.error(request,"password dosen't match")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist!")
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist!")


        myuser.save()

        messages.success(request,"account sucessfully created")
        return redirect("login")
    
    return render(request,"login_sys/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]

        user = authenticate(username=username, password=password)

        if user is not None:
            user_login(request,user)
            return render(request,"login_sys/index.html")

        else:
            messages.error(request,"Bad Cridentials")
            return redirect("signup")   

    return render(request,"login_sys/login.html")

def logout(request):
    user_logout(request)
    return render(request,"login_sys/logout.html")
