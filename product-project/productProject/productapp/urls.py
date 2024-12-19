from  django.urls import path
from  . import views
urlpatterns=[
path('',views.BookListView.as_view(),name='booklist'),
path('cr/',views.BookCreateView.as_view(),name='createbook'),
path('dl/<int:pk>/',views.BookDetailsView.as_view(),name='detailbook'),
path('up/<int:pk>/',views.BookUpdateView.as_view(),name='updatebook'),
path('dt/<int:pk>/',views.BookDeleteView.as_view(),name='deletebook')




]