# models.py
from django.db import models # Change this from 'from djongo import models'

class Product(models.Model):
    # Remove the manual _id = models.ObjectIdField() 
    # The new backend handles ObjectIds automatically.
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name