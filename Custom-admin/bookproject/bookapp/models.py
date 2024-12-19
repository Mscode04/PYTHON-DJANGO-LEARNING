from django.db import models

# Create your models here.

class Auther(models.Model):
    name = models.CharField(max_length=200, null=True, default="Unknown Author")

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    auther = models.ForeignKey(
        Auther,
        on_delete=models.CASCADE,
        null=True,  # Temporarily allow nulls
        default=None  # Or assign an Auther ID directly if known
    )
    price = models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media',null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.title)
