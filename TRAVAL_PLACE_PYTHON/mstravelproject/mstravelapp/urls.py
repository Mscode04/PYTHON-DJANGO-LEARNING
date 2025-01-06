
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CountryListView,
    DistrictListView,
    PlaceCreateView,
    PlaceDetailView,
    PlaceUpdateView,
    PlaceDeleteView,
    StateListView,
    create_place,
    update_travelplace,
    delete_travelplace,
    list_travelplaces,
)
from mstravelapp import views

urlpatterns = [
    # API endpoints
    path('api/places/', PlaceCreateView.as_view(), name='place-list-create'),
    path('api/places-detail/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('api/places-update/<int:pk>/', PlaceUpdateView.as_view(), name='place-update'),
    path('api/places-delete/<int:pk>/', PlaceDeleteView.as_view(), name='place-delete'),
    
    path('register/', views.register, name='register'),
    path('api/countries/', CountryListView.as_view(), name='country-list'),
    path('api/states/', StateListView.as_view(), name='state-list'),
    path('api/districts/', DistrictListView.as_view(), name='district-list'),
    
    # Function-based views
    path('create-place/', create_place, name='create-place'),
    path('', list_travelplaces, name='list-travelplaces'),
    path('travelplaces-update/<int:id>/', update_travelplace, name='update-travelplace'),
    path('travelplaces-delete/<int:id>/', delete_travelplace, name='delete-travelplace'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)