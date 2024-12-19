
from django.urls import path
from . import  views
urlpatterns=[

# path('register/',views.RegisterUser,name='register'),
# path('login/',views.LoginUser,name='login'),
# path('logout/',views.LogOut,name='logout'),
# path('home/',views.HomePage,name='home'),
path('register/',views.UserRegistration,name='register'),
path('login/',views.LoginPage,name='login'),
path('adminv/',views.adminView,name='admin_view'),
path('userv/',views.userView,name='user_view'),

]