from django.db import models

# Create your models here.


# 1.在models.py中书写一个类
class User(models.Model):
    # 创建字段
    id = models.AutoField(primary_key=True, verbose_name='主键')  # 等价于id int primary_key auto_increment
    username = models.CharField(max_length=32, verbose_name='用户名')  # 等价于 username varchar(32)
    password = models.CharField(max_length=64, verbose_name='密码')  # 等价于password int()
    """
    CharField 不指定max_length参数会报错
    """
    # 新添加的字段
    # age = models.IntegerField(verbose_name='年龄')
    # # 设置字段可以为空
    # info = models.CharField(max_length=32, verbose_name='个人简介', null=True)
    # # 设置字段的默认值
    # hobby = models.CharField(max_length=32, verbose_name='爱好', default='study')
    def __str__(self):
        return '%s' % self.username


class Author(models.Model):
    # 由于一张表必须有一个主键字段，并且一般情况都叫id字段
    # orm会自动创建主键字段名为id
    # 主键字段没有额外要求的时候，可以省略

    username = models.CharField(max_length=32)  # 等价于 username varchar(32)
    password = models.IntegerField()
