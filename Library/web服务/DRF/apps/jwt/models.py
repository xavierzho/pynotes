from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.jpg')
