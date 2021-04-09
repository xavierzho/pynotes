from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 单个字段，有索引，有唯一
        # 多个字段，有联合索引，联合唯一
        abstract = True  # 抽象表，不再数据库上建表


class Book(BaseModel):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(on_delete=models.DO_NOTHING, to='Publish', db_constraint=False)
    authors = models.ManyToManyField(to='Author', db_constraint=False)

    class Meta:
        verbose_name_plural = '书表'
        verbose_name = '书表'

    def __str__(self):
        return self.name

    @property
    def publish_name(self):
        return self.publish.name

    @property
    def author_list(self):
        author_list = self.authors.all()
        # ll = []
        # for author in author_list:
        #     # ll.append({'name': author.name, 'sex': author.sex})
        #     # 在choices参数中需要显示真实内容的时候使用以下方法
        #     ll.append({'name': author.name, 'sex': author.get_sex_display()})
        return [{'name': author.name, 'sex': author.get_sex_display()} for author in author_list]


class Publish(BaseModel):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = '出版社表'
        verbose_name = '出版社表'

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=32)
    sex = models.IntegerField(choices=((1, '男'), (2, '女'), (3, '其他')))
    detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, db_constraint=False)

    # detail = models.ForeignKey(to='AuthorDetail', unique=True, on_delete=models.CASCADE, db_constraint=False)
    class Meta:
        verbose_name_plural = '作者表'
        verbose_name = '作者表'

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = '作者详情表'
        verbose_name = '作者详情表'

    def __str__(self):
        return self.phone

