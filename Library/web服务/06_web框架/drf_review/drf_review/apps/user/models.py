from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_delete = models.BooleanField(default=0)
    phone = models.CharField(max_length=32)
    icon = models.FileField(upload_to='icon/default.jpg')
