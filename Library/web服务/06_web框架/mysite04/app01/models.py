from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    # 性别
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他')

    )
    gender = models.IntegerField(choices=gender_choices)
#     """
#     该gender字段还是存储数字，如果是对应数字元组内的数据，那么可以非常轻松的获取到数字的对应内容
#     1.gender字段存的数字不在列举的元组范围内
#
#     2.如果在 如何获取对应的信息
#     """
#     score_choices = (
#         ('A', '优秀'),
#         ('B', '良好'),
#         ('C', '及格'),
#         ('D', '不合格'),
#     )
#     # 保证字段类型跟列举出来的元组第一个数据类型一致即可
#     score = models.CharField(max_length=32, choices=score_choices, null=True)
#
#
# class Book(models.Model):
#     name = models.CharField(max_length=32)
#     authors = models.ManyToManyField(to='Authors',
#                                      through='Book2Author',
#                                      through_fields=('book', 'author')
#                                      )
#
#
# class Authors(models.Model):
#     name = models.CharField(max_length=32)
#     # book = models.ManyToManyField(to='Book',
#     #                               through='Book2Author',
#     #                               through_fields=('author', 'book')
#     #                               )
# """
# through_fields 字段先后顺序
#     判断本质:
#         通过第三张表查询对应的表,需要用哪个字段就把哪个字段放前面
#     判断优化:
#         当前表是谁,就把对应的表名放前面
# """
#
# class Book2Author(models.Model):
#     book = models.ForeignKey(to='Book')
#     author = models.ForeignKey(to='Authors')


class Book(models.Model):
    title = models.CharField(max_length=32)

