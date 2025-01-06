from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import requests 
from .forms import *
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
    
    
    
class RecipeSearch(generics.ListAPIView):
    queryset=Recipes.objects.all()
    serializer_class=RecipesSeriallizers
    def get_queryset(self):
        name=self.kwargs.get('Name')
        return Recipes.objects.filter(Name__icontains=name)
        
    
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            try:               
                form.save()
                data = form.cleaned_data
                files = {'Recipe_img': request.FILES['Recipe_img']}
                api_url = 'http://127.0.0.1:8000/create/'
                response = requests.post(api_url, data=data, files=files)
                if response.status_code == 201:
                    messages.success(request, 'Recipe Added Successfully')
                    return redirect('/')
                else:
                    return redirect('/')
            except requests.RequestException as e:
                pass
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = RecipeForm()
    return render(request, 'create-recipe.html', {'form': form})
    
    



    
def update_recipe(request, id):
    # Fetch the recipe to be updated
    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        recipe = response.json()

        if request.method == 'POST':
            name = request.POST['Name']
            prep_time = request.POST["Prep_time"]
            difficulty = request.POST['Difficulty']
            vegetarian = request.POST.get('Vegetarian', 'false') == 'true'
            description = request.POST['Description']
            image = request.FILES.get('Recipe_img', None)  # Handle image upload

            # Prepare data and files for the PUT request
            data = {
                'Name': name,
                'Prep_time': prep_time,
                'Difficulty': difficulty,
                'Vegetarian': vegetarian,
                'Description': description,
            }
            files = {'Recipe_img': image} if image else {}

            # Update the recipe through the API
            api_url = f'http://127.0.0.1:8000/update/{id}/'
            update_response = requests.put(api_url, data=data, files=files)

            if update_response.status_code == 200:
                messages.success(request, 'Recipe updated successfully')
                return redirect("/")
            else:
                messages.error(request, f"Error updating recipe: {update_response.status_code}")
        else:
            return render(request, 'recipe-update.html', {'recipe': recipe})
    
    else:
        messages.error(request, 'Recipe not found.')
        return redirect('/')
    
    
from django.shortcuts import render
def index(request):
    recipes = Recipes.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search', '')
        api_url = f'http://127.0.0.1:8000/search/{search}/'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return render(request, 'index.html', {'data': data})
            else:
                return render(request, 'index.html')
        except requests.RequestException as e:
            return render(request, 'index.html')
    else:
        paginator = Paginator(recipes, 6)  # Display 6 recipes per page
        page = request.GET.get('page', 1)
        try:
            paginated_recipes = paginator.page(page)
        except PageNotAnInteger:
            paginated_recipes = paginator.page(1)
        except EmptyPage:
            paginated_recipes = paginator.page(paginator.num_pages)
        
        context = {'recipes': paginated_recipes}
        return render(request, 'index.html', context)


def recipe_fetch(request, id):
    import requests

    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        # Split ingredients by commas, strip whitespace, and filter out empty items
        ingredients = [ingredient.strip() for ingredient in data['Description'].split(',') if ingredient.strip()]
        return render(request, 'recipe-fetch.html', {'recipes': data, 'ingredients': ingredients})
    
    return render(request, 'recipe-fetch.html', {'error': 'Recipe not found or error fetching details.'})



def recipe_delete(request,id):
    api_url=f'http://127.0.0.1:8000/delete/{id}/' 
    response=requests.delete(api_url)
    if response.status_code==200:
        print(f'item with id{id} has been deleted')
    else:
        print(f'failed to delete {response.status_code}')    
    return redirect('/')    