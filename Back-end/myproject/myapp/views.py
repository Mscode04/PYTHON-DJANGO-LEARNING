from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
# Create your views here.
class RecipeCreateView(generics.ListCreateAPIView):
    queryset=Recipes.objects.all()
    serializer_class=RecipesSeriallizers
    permission_classes=[AllowAny]
    
    
class RecipeDeatail(generics.RetrieveAPIView):
    queryset=Recipes.objects.all()
    serializer_class=RecipesSeriallizers
    
    
    
class RecipeUpdateView(generics.RetrieveUpdateAPIView):
    queryset=Recipes.objects.all()
    serializer_class=RecipesSeriallizers
    
    
    
class RecipeDelete(generics.DestroyAPIView):
    queryset=Recipes.objects.all()
    serializer_class=RecipesSeriallizers