from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from django.contrib import messages
from .models import Place,Country, State, District
from .serializers import PlaceSerializer,CountrySerializer, StateSerializer, DistrictSerializer
from .forms import PlaceForm,UserRegistrationForm
import requests

# API Views
class PlaceCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]


class PlaceDetailView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Save the form locally
                form.save()

                # Prepare the data for API submission
                data = form.cleaned_data
                files = {'place_image': request.FILES['place_image']}
                api_url = 'http://127.0.0.1:8000/api/places/'  # Replace with your API endpoint
                response = requests.post(api_url, data=data, files=files)

                if response.status_code == 201:  # Successful creation
                    messages.success(request, 'Place Added Successfully')
                    return redirect('/')
                else:
                    return redirect('/')
            except requests.RequestException as e:
                messages.error(request, 'An error occurred while submitting to the API.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = PlaceForm()

    return render(request, 'create-place.html', {'form': form})


def update_travelplace(request, id):
    try:
        # Fetch the place to be updated from the database
        place = Place.objects.get(pk=id)
    except Place.DoesNotExist:
        messages.error(request, 'Travel Place not found.')
        return redirect('list-travelplaces')

    # API endpoint for the update request
    api_url = f'http://127.0.0.1:8000/api/places-update/{id}/'

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            # Collect the form data
            updated_data = form.cleaned_data
            updated_files = {'place_image': request.FILES.get('place_image', None)} if request.FILES.get('place_image') else {}

            # Send PUT request to update the travel place
            response = requests.put(api_url, data=updated_data, files=updated_files)

            if response.status_code == 200:
                messages.success(request, 'Travel Place updated successfully!')
                return redirect('list-travelplaces')
            else:
                messages.error(request, f"Error updating travel place: {response.status_code}")
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = PlaceForm(instance=place)

    return render(request, 'update-travelplace.html', {'form': form, 'place': place})


def delete_travelplace(request, id):
    api_url = f'http://127.0.0.1:8000/api/places-delete/{id}/'
    response = requests.delete(api_url)

    if response.status_code == 204:  # No Content
        messages.success(request, 'Travel Place deleted successfully!')
    else:
        messages.error(request, 'Failed to delete Travel Place.')
    return redirect('list-travelplaces')


def list_travelplaces(request):
    travelplaces = Place.objects.all()
    return render(request, 'list-travelplaces.html', {'travelplaces': travelplaces})


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateListView(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        country_id = self.request.GET.get('country_id')
        return State.objects.filter(country_id=country_id)

class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        state_id = self.request.GET.get('state_id')
        return District.objects.filter(state_id=state_id)

def register(request):
    countries = Country.objects.all()  # Get all countries
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('/')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form, 'countries': countries})



