from django.db import models

# Create your models here.
class MyTable(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)
