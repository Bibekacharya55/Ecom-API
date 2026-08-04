from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    discount_percentage = models.FloatField()

    rating = models.FloatField()

    images =  models.ImageField(upload_to="products/")

    def __str__(self):
        return self.title