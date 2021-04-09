from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.name


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    user_type = models.IntegerField(choices=((1, '超级用户'), (2, '普通用户'), (3, '其他用户')))


class UserToken(models.Model):
    token = models.CharField(max_length=128)
    user = models.OneToOneField(to='Users', on_delete=models.CASCADE)