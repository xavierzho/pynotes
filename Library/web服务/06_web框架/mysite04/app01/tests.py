from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite04.settings")
    import django
    django.setup()

    from app01 import models
    # models.User.objects.create(username='jones', age=18, gender=1)
    # models.User.objects.create(username='tins', age=22, gender=2)
    # models.User.objects.create(username='qua', age=23, gender=3)
    # models.User.objects.create(username='tank', age=33, gender=4)
    # 存储时，没有列举的数据也能存储(范围还是按照字段类型决定)

    # 取
    # user_obj = models.User.objects.filter(pk=1).first()
    # print(user_obj.gender)
    # 只要时choices参数，要获取对应的信息，语法格式：get_xx_display()
    # print(user_obj.get_gender_display())

    # user_obj = models.User.objects.filter(pk=4).first()
    # # 如果没有对应关系，字段是什么就返回什么
    # print(user_obj.get_gender_display())
    models.Book.objects.filter(pk__gt=1000).delete()
