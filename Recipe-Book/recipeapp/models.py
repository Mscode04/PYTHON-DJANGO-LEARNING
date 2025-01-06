from datetime import timedelta
from django.db import models

# Create your models here.
class Recipes(models.Model):
    Name=models.CharField(max_length=200)
    Prep_time=models.DurationField(default=timedelta(minutes=120))
    DIFFICULTY_CHOICES=[
        (1,'EASY'),
        (2,'MEDIUM'),
        (3,'HARD'),
    ]
    Difficulty=models.IntegerField(choices=DIFFICULTY_CHOICES)
    Vegetarian=models.BooleanField()
    Recipe_img=models.ImageField(upload_to='recipe/')
    Description=models.CharField(max_length=5000)