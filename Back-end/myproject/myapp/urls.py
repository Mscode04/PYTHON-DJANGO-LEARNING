from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create/',RecipeCreateView.as_view(),name='create-recipe'),
    path('detail/<int:pk>/',RecipeDeatail.as_view(),name='detail-recipe'),
    path('update/<int:pk>/',RecipeUpdateView.as_view(),name='update-recipe'),
    path('delete/<int:pk>/',RecipeDelete.as_view(),name='delete-recipe'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
