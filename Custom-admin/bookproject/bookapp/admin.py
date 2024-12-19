from django.contrib import admin

# Register your models here.
from .models import Book,Auther

admin.site.register(Book)
admin.site.register(Auther)