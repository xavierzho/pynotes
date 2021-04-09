from django.db import models
from django.db.models.fields import Field


class MyCharField(Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        # 调用父类的init方法
        super().__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        返回真正的数据类型及各种约束条件
        :param connection:
        :return:
        """
        return 'char(%s)' % self.max_length


class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    register_time = models.DateField()  # 日期字段

    # register_time = models.DateTimeField()  # 年月日时分秒字段

    # 自定义字段使用
    my_field = MyCharField(max_length=16, null=True)

    def __str__(self):
        return '对象：%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)
    # 库存
    inventory = models.IntegerField(default=500)
    # 卖出
    sell = models.IntegerField(default=500)

    # 一对多
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    # 多对多
    author = models.ManyToManyField(to='Author')

    def __str__(self):
        return '对象：%s' % self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return '对象：%s' % self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    info = models.CharField(max_length=64)
