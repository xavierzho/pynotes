from django.db import models


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=64, null=True, default='')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

