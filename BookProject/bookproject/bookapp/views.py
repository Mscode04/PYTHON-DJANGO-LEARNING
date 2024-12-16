from django.shortcuts import render,redirect
from django.template.defaultfilters import title

# Create your views here.

from  .models import Book


def createBook(reqeust):
    books = Book.objects.all()
    if reqeust.method=='POST':
        title=reqeust.POST.get('title')
        price=reqeust.POST.get('price')
        book=Book(title=title,price=price)
        book.save()

    return render(reqeust,'book.html',{'books':books})



def listBook(reqeust):
    books=Book.objects.all()
    return render(reqeust,'listbook.html',{'books':books})

def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return  render(request,'detailview.html',{'book':book})


def updatebook(reqeust,book_id):
    book=Book.objects.get(id=book_id)
    if reqeust.method=='POST':
        title=reqeust.POST.get('title')
        price=reqeust.POST.get('price')
        book.title=title
        book.price=price
        book.save()
        return  redirect('/')

    return render(reqeust,'updateview.html',{'book':book})


def deleteview(reqeust,book_id):
    book = Book.objects.get(id=book_id)
    if reqeust.method == 'POST':
        book.delete()
        return redirect('/')
    return render(reqeust,'deleteview.html',{'book':book})









