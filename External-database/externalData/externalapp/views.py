from django.shortcuts import render

# Create your views here.
from .models import MyTable

def TableShow(request):
    table=MyTable.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        table1=MyTable(name=name,email=email)
        table1.save()
    return render(request,'table.html',{'table':table})












