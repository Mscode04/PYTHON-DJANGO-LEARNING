from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipes
        fields='__all__'