from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from django.template.defaultfilters import title

# Create your views here.

from  .models import Book
from  .form import AutherForm,BookForm

# def createBook(reqeust):
#     books = Book.objects.all()
#     if reqeust.method=='POST':
#         title=reqeust.POST.get('title')
#         price=reqeust.POST.get('price')
#         book=Book(title=title,price=price)
#         book.save()
#
#     return render(reqeust,'book.html',{'books':books})
























def listBook(reqeust):
    books=Book.objects.all()
    paginator=Paginator(books,3)
    page_number=reqeust.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.get_page(page_number.num_pages)

    return render(reqeust,'listbook.html',{'books':books,'page':page})

def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return  render(request,'detailview.html',{'book':book})


# def updatebook(reqeust,book_id):
#     book=Book.objects.get(id=book_id)
#     if reqeust.method=='POST':
#         title=reqeust.POST.get('title')
#         price=reqeust.POST.get('price')
#         book.title=title
#         book.price=price
#         book.save()
#         return  redirect('/')
#
#     return render(reqeust,'updateview.html',{'book':book})


def deleteview(reqeust,book_id):
    book = Book.objects.get(id=book_id)
    if reqeust.method == 'POST':
        book.delete()
        return redirect('/')
    return render(reqeust,'deleteview.html',{'book':book})




def createBook(request):
    books=Book.objects.all()
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=BookForm()
    return render(request,'book.html',{'form':form,'books':books})



def createAuther(request):
    if request.method=='POST':
        form=AutherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=AutherForm()
    return render(request,'auther.html',{'form':form})

def updatebook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=BookForm(instance=book)
    return render(request,'updateview.html',{'form':form})

def index(request):
    return  render(request,'base.html')

def SerchBook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]

    context={'books':books,
             'query':query}

    return  render(request,'search.html',context)



