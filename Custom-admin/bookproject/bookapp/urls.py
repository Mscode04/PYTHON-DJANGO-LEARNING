
from django.urls import path


from . import  views
urlpatterns=[

path('create',views.createBook,name='create'),
    path('',views.listBook,name='booklist'),
    path('view/<int:book_id>/',views.detailsview,name='details'),
    path('upview/<int:book_id>/',views.updatebook,name='update'),
    path('dview/<int:book_id>/',views.deleteview,name='delete'),
    path('auther/',views.createAuther,name='auther'),
    path('in/',views.index,name='index'),
    path('search/',views.SerchBook,name='search'),

]