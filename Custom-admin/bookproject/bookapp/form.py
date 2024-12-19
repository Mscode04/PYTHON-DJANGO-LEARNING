from django import  forms
from  .models import Book,Auther


class AutherForm(forms.ModelForm):
    class Meta:
        model=Auther
        fields=['name']
        widgets = {
            'auther': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the auther name'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'auther':forms.Select(attrs={'class':'form-control','placeholder':'Enter the auther name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the price'}),
        }














