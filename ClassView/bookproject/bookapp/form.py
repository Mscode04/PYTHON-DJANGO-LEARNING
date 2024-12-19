from django import  forms
from  .models import Book,Auther


class AutherForm(forms.ModelForm):
    class Meta:
        model=Auther
        fields=['name']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'














