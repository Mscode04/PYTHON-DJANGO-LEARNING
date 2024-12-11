from django.shortcuts import render
from  django.http import HttpResponse

# def fun1(request):
#     return HttpResponse("Hello fun1 http req")
# def fun2(request):
#     return HttpResponse("Hello fun2 http req")

def fun2(request):
    return render(request,'intex.html')

def fun1(request):
    return render(request,'main.html')

