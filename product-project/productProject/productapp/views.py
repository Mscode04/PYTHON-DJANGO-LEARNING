from django.shortcuts import render
from  django.urls import reverse_lazy
# Create your views here.
from  .models import Book
from  django.views.generic import  CreateView,ListView,DetailView,UpdateView,DeleteView

class BookCreateView(CreateView):
    model = Book
    template_name = 'home.html'


    success_url =reverse_lazy('booklist')

class BookListView(ListView):
    model = Book
    template_name = 'listview.html'
    context_object_name = 'books'

class BookDetailsView(DetailView):
    model = Book
    template_name = 'detailview.html'
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'updateview.html'
    fields = ['title','price']
    success_url =reverse_lazy('booklist')



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'deleteview.html'
    context_object_name = 'book'
    success_url =reverse_lazy('booklist')


