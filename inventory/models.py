from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    specs = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name