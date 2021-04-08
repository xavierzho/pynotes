from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()