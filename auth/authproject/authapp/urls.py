
from django.urls import path
from . import  views
urlpatterns=[

path('register/',views.RegisterUser,name='register'),
path('login/',views.LoginUser,name='login'),
path('logout/',views.LogOut,name='logout'),
path('home/',views.HomePage,name='home'),


]