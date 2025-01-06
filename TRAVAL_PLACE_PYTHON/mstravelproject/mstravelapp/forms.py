from django import forms
from .models import Place
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__' 
        
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):


    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password',]


        
