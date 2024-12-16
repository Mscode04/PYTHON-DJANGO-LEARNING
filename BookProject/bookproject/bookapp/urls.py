
from django.urls import path
from . import  views
urlpatterns=[

path('',views.createBook),
    path('list/',views.listBook),
    path('view/<int:book_id>/',views.detailsview,name='details'),
    path('upview/<int:book_id>/',views.updatebook,name='update'),
    path('dview/<int:book_id>/',views.deleteview,name='delete'),

]