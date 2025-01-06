from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django import forms
class Place(models.Model):
    name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField(max_length=500)
    place_image = models.ImageField(upload_to='places/')
    description = models.TextField(max_length=5000)
    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)  # Add this line if you want to keep the name field
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)

    # Add related_name to avoid conflict with the default 'user_permissions' and 'groups' fields
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Custom reverse relationship
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set',  # Custom reverse relationship
        blank=True
    )

    def __str__(self):
        return self.username
    
