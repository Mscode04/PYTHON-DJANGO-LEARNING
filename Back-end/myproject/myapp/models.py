from datetime import timedelta
from django.db import models

# Create your models here.
class Recipes(models.Model):
    Name=models.CharField(max_length=200)
    Prep_time=models.DurationField(default=timedelta(minutes=120))
    Description=models.CharField(max_length=5000)
    Recipe_img=models.ImageField(upload_to='recipe/')