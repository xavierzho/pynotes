from django.db import models

# Create your models here.


# 创建表关系，先将基表创建出来，然后在添加外键字段
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # 数字位置一共8位，小数点后面占2位
    """
    图书和出版社是一对多的关系,并且书是多的一方，所以外键放在书表里面
    """
    publish = models.ForeignKey(to='Publish')  # 默认与Publish表的外键字段做外键关联
    """
    如果字段对应的是ForeignKey ，orm会自动在publish后面添加_id
    如果自己添加了_id，还是会自动添加_id
    凡是定义ForeignKey的时候就不需要添加_id后缀
    """

    """
    书和作者是多对多的关系，orm提供外键字段建在任意一方均可，推荐建在查询频率较高的一方
    """
    authors = models.ManyToManyField(to='Author')  # 这是个虚拟字段，用来告诉orm 书籍表和作者表是多对多的关系，让orm自动帮你创建第三张关系表


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    """
    作者与作者详情是一对一关系，外键字段建在任意一方即可，推荐建在查询频率较高的表
    """
    author_detail = models.OneToOneField(to='AuthorDetail')


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 或者直接用字符类型
    addr = models.CharField(max_length=32)
