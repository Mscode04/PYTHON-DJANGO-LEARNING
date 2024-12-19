from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.

def RegisterUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstName')
        last_name=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirmPassword')
        if confirm==password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'The user already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'The email already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return  redirect('login')
        else:
            messages.info(request, 'This password is not correct')
    return render(request,'register.html')
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User not found')
            return redirect('login')
    return render(request, 'login.html')

def LogOut(request):
    auth.logout(request)
    return redirect('login')


def HomePage(request):

    return render(request, 'home.html')































