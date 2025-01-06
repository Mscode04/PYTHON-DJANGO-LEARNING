from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path
from . import views
urlpatterns = [
    path('create/',RecipeCreateView.as_view(),name='create-recipe'),
    path('detail/<int:pk>/',RecipeDeatail.as_view(),name='detail-recipe'),
    path('update/<int:pk>/',RecipeUpdateView.as_view(),name='update-recipe'),
    path('delete/<int:pk>/',RecipeDelete.as_view(),name='delete-recipe'),
    path('search/<str:Name>/',RecipeSearch.as_view(),name='search-recipe'),
    
    
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipe_fetch/<int:id>/', views.recipe_fetch, name='recipe_fetch'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('recipe_delete/<int:id>/', views.recipe_delete, name='recipe_delete'),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)