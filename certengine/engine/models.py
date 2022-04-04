from django.db import models

# Create your models here.

class Car(models.Model):
    object_id = models.TextField()
    maker = models.CharField(max_length=100)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # Add a __str__ method to the Car class.
    def __str__(self):
        return f'{self.maker} {self.model} {self.year} {self.category}'