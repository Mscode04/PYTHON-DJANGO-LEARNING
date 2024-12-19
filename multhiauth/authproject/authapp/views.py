
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile,LoginTable

# Create your views here.

def UserRegistration(request):
    login_table=LoginTable()
    userprofile=UserProfile()
    if request.method=='POST':
        userprofile.username=request.POST['username']
        userprofile.password=request.POST['password']
        userprofile.password2=request.POST['password1']

        login_table.username=request.POST['username']
        login_table.password=request.POST['password']
        login_table.password2=request.POST['password1']
        login_table.type='user'

        if request.POST['password']==request.POST['password1']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Completed')
            return redirect('login')
        else:
            messages.info(request, 'password not match')
            return redirect('register')
    return render(request,'register.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=LoginTable.objects.filter(username=username,password=password,type='user').exists()
        try:
            if user is not None:
                user_details=LoginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type
                if type=='user':
                    request.session['username']=user_name
                    return redirect('user_view')

                elif type=='admin':
                    request.session['username']=user_name
                    return redirect('admin_view')

            else:
                messages.error(request,'invalid username or password')
        except :
            messages.error(request,'invalid role')
    return render(request,'login.html')


def adminView(request):
    user_name=request.session['username']
    return render(request,'admin_view.html', {'user_name': user_name})

def userView(request):
    user_name = request.session['username']
    return render(request,'user_view.html',{'user_name': user_name})


