from django.test import TestCase

# Create your tests here.
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite03.settings")
    import django
    django.setup()
    # 下面就可以测试django三个py文件了
    # 所有的代码都必须等待环境准备完毕，才能书写
    from app03 import models
    # models.User.objects.all()

    # 增加
    # res = models.User.objects.create(name='jones', age=22, register_time='2002-1-21')
    # print(res)
    #######################################
    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='tins',age=23, register_time=ctime)
    # user_obj.save()

    # 删除
    # res = models.User.objects.filter(pk=2).delete()
    # print(res)
    #####################################
    # data_obj = models.User.objects.filter(pk=1).first()
    # data_obj.delete()

    # 修改
    # data_obj = models.User.objects.filter(pk=5)
    ################################################
    # data_obj = models.User.objects.get(pk=5)
    # get返回的是当前的数据对象，一旦数据不存在直接报错，而filter则不会
    # data_obj.name = 'jonescy'
    # data_obj.save()

    # 查询
    # res = models.User.objects.all().first()
    # print(res)
    # res1 = models.User.objects.all().last()
    # print(res1)

    # values()
    # data_obj = models.User.objects
    # print(data_obj.values('name', 'age'))
    # <QuerySet [{'name': 'jones', 'age': 22}, {'name': 'TinsQua', 'age': 23}, {'name': 'jonescy', 'age': 22}, {'name': 'tins', 'age': 23}]>
    # print(data_obj.values_list('name', 'age'))

    # distinct()
    # res = models.User.objects.values('name', 'age').distinct()
    # print(res)

    # order_by()
    # res = models.User.objects.order_by('-age')
    # print(res)

    # reverse()
    # res = models.User.objects.all()
    # res1 = models.User.objects.order_by('age').reverse()
    # print(res, '\n', res1)

    # count()
    # res = models.User.objects.count()
    # print(res)

    # exclude()
    # res = models.User.objects.exclude(name='jones')
    # print(res)

    # exists()
    # res = models.User.objects.filter(pk=1).exists()
    # print(res)

    # # 双下划线查询
    # # 1.年龄大于30的数据
    # res = models.User.objects.filter(age__gt=30)
    # print(res)
    # # 2.年龄小于30的数据
    # res = models.User.objects.filter(age__lt=30)
    # print(res)
    # # 3.年龄大于等于33的数据
    #
    # res = models.User.objects.filter(age__gte=33)
    # print(res)
    # # 4.年龄小于等于33的数据
    #
    # res = models.User.objects.filter(age__lte=33)
    # print(res)
    # # 5.年龄18 或者32 或者40 的
    # res = models.User.objects.filter(age__in=[22, 33, 40])
    # # 6.年龄在18~30之间的
    # res1 = models.User.objects.filter(age__range=[18, 40])
    # print(res1)
    # # 7.查询名字含有n的数据
    # res2 = models.User.objects.filter(name__contains='t')
    # print(res2)
    #
    # # 忽略大小写：
    # res3 = models.User.objects.filter(name__icontains='t')
    # print(res3)
    #
    # # 8.查询名字以j开头的
    # res4 = models.User.objects.filter(name__startswith='j')
    # print(res4)
    #
    # # 9.查询出注册时间是2002-1的数据
    # res5 = models.User.objects.filter(register_time__year=2002).filter(register_time__month=1)
    # print(res5)

    # # 一对多的外键增删改查
    # # 增
    # # 1. 直接写实际字段 id
    # models.Book.objects.create(title='论语', price=332.22, publish_id=1)
    # models.Book.objects.create(title='中庸', price=122.22, publish_id=2)
    # models.Book.objects.create(title='老子', price=222.22, publish_id=1)
    # # 2. 虚拟字段 对象
    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.create(title='水浒传', price=69.99, publish=publish_obj)
    #
    # # 删除  默认级联更新级联删除
    # models.Publish.objects.filter(pk=2).delete()
    #
    # # 改
    # # 1. 直接写实际字段 id
    # models.Book.objects.filter(pk=6).update(publish_id=2)
    # # 2. 虚拟字段 对象
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.filter(pk=6).update(publish=publish_obj)
    #
    # # 查
    #
    # # 多对多的增删改查 -- 实际上就是第三张关系表的增删改查
    # # 给书籍绑定作者
    # # 方式一，直接操作id
    # book_obj1 = models.Book.objects.filter(pk=10).first()
    # # print(book_obj.author)   # 类似于操作第三张关系表
    # book_obj1.author.add(1)  # 给书籍id为6的书籍绑定一个主键为1的作者
    # book_obj1.author.add(2, 3)
    # # 方式二，
    # book_obj2 = models.Book.objects.filter(pk=11).first()
    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # book_obj2.author.add(author_obj, author_obj1)
    # """
    # add给第三张关系表添加数据
    #     括号内可以传数字，也可以传对象，并且支持添加多个
    # """
    #
    # # 删除
    # book_obj.author.remove(1, 3)
    # book_obj.author.remove(author_obj, author_obj1)
    # """
    # remove
    #     括号内可以传数字，也可以传对象，并且支持添加多个
    # """
    #
    # # 修改
    # book_obj.author.set([1, 3])
    # book_obj.author.set([author_obj1, author_obj])
    # """
    # set
    #     括号内必须是可迭代对象,写元组或者列表，对象内传入数字或者对象
    #     先删除后增加
    # """
    # # 清空，在第三张关系表中，清空2者所有的绑定关系
    # book_obj.author.clear()

    # 基于对象的跨表查询
    # 1.查询书籍主键为1的出版社
    # book_obj = models.Book.objects.filter(pk=10).first()
    # # 书查出版社 正向
    # publish_obj = book_obj.publish
    # print(publish_obj)

    # # 2.查询主键为2的作者
    # book_obj = models.Book.objects.filter(pk=10).first()
    # # 书查作者 正向
    # # author_obj = book_obj.author # app03.Author.None
    # author_obj = book_obj.author.all()  # <QuerySet [<Author: Author object>, <Author: Author object>, <Author: Author object>]>
    # print(author_obj)

    # # 3.查询作者jones的电话号码
    # author_obj = models.Author.objects.filter(name='jones').first()
    # # 作者查作者详情 正向
    # author_detail_obj = author_obj.author_detail
    # print(author_detail_obj)
    # print(author_detail_obj.phone)
    # print(author_detail_obj.info)
    """
    基于对象正向查询
        在写orm语句的时候写sql语句一样，不要企图一次性将orm语句写完，看一点写一点
        正向什么时候加.all()
            当结果可能有多个的时候需要加.all()
            如果数据是一个则直接拿到数据对象
    """
    # # 4.查询东方出版社出版的书
    # publish_obj = models.Publish.objects.filter(name='东方出版社').first()
    # # 出版社查书  反向
    # # book_obj = publish_obj.book_set  # app03.Book.None
    # book_obj = publish_obj.book_set.all()
    # print(book_obj)

    # # 5.查询作者是jones写过的书
    # author_obj = models.Author.objects.filter(name='jones').first()
    # # 作者查书 反向
    # # book_obj = author_obj.book_set  # app03.Book.None
    # book_obj = author_obj.book_set.all()
    # print(book_obj)

    # # 6.查询手机号是110的作者姓名
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
    # author_obj = author_detail_obj.author
    # print(author_obj.name)
    """
    基于对象的反向查询
        当查询结果可以有多个的时候必须加_set.all()
        当查询结果只有一个的时候不需要加_set.all()
    """

    # 基于双下划线的跨表查询

    # # 1.查询jones 的手机号和作者名（一行代码）-> 正向查询
    # res = models.Author.objects.filter(name='jones').values('author_detail__phone', 'name')
    # print(res)
    # # 方向查询
    # res = models.AuthorDetail.objects.filter(author__name='jones').values('phone', 'author__name')
    # print(res)
    #
    # # 2. 查询书籍主键为10的出版社名称和书名->正向查询
    # res = models.Book.objects.filter(pk=10).values('title', 'publish__name')
    # print(res)
    # # 反向查询
    # res = models.Publish.objects.filter(book__pk=10).values('name', 'book__title')
    # print(res)
    #
    # # 3.查询书籍主键为10的作者姓名
    # res = models.Book.objects.filter(pk=10).values('author__name')
    # print(res)
    # # 反向查询
    # res = models.Author.objects.filter(book__pk=10).values('name')
    # print(res)
    #
    # # 4.查询书籍主键是10的作者的手机号
    # res = models.Book.objects.filter(pk=10).values('author__author_detail__phone')
    # print(res)

    # # 聚合查询  aggregate
    # from django.db.models import Max, Min, Sum, Count, Avg
    # # 1.统计书的平均价格
    # # res = models.Book.objects.aggregate(Avg('price'))
    # # print(res)
    # # 2.上述方法一次使用
    # res1 = models.Book.objects.aggregate(Max('price'), Min('price'), Sum('price'), Count('pk'))
    # print(res1)

    # # 分组查询   annotate
    # from django.db.models import Max, Min, Sum, Count, Avg
    # # 1.统计每一本书的作者个数
    # res = models.Book.objects.annotate(author_num=Count('author')).values('title', 'author_num')  # models后面点什么 就是按什么分组
    # """
    # author_num 是我们自己定义的字段，用来存储统计出来的每本书对应的作者个数
    # """
    # print(res)
    #
    # # 2.统计每个出版社卖的最便宜的书的价格
    # res = models.Publish.objects.annotate(min_price=Min('book__price')).values('name', 'min_price')
    # print(res)
    #
    # # 3.统计不止一个作者的图书
    # res = models.Book.objects.annotate(author_num=Count('author')).filter(author_num__gt=1).values('title', 'author_num')
    # """
    # 只要orm语句得出的结果还是一个queryset对象，就可以无限的使用queryset对象封装的方法
    # """
    # print(res)
    #
    # # 4.查询每个作者出的书的总价格
    # res = models.Author.objects.annotate(sum_price=Sum('book__price')).values('name', 'sum_price')
    # print(res)
    # """
    # 如果需要按照指定的字段分组如何处理？
    #     models.Book.objects.values('price').annotate()
    # """

    # # F与Q查询
    # # 1.卖出数大于库存数的书籍
    # # F查询
    # from django.db.models import F, Q
    # """
    # 能够直接获取表中某个字段对应的数据
    # """
    # res = models.Book.objects.filter(sell__gt=F('inventory'))
    # print(res)
    #
    # # 2.将所有的书籍的价格提升50元
    # res = models.Book.objects.update(price=F('price')+50)
    # print(res)
    #
    # # 3.将所有书的名称后面加上爆款两个字
    # """
    # 在操作字符类型的数据的时候，F不能直接做到字符串的拼接,需要借助Concat和Value模块
    # """
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # models.Book.objects.update(title=Concat(F('title'), Value('(爆款)')))
    #
    # # Q 查询
    # # 1.查询卖出数大于100，或者价格小于200的书籍
    # res = models.Book.objects.filter(sell__gt=100, price__lt=200)  # and
    # res = models.Book.objects.filter(Q(sell__gt=100) | Q(price__lt=200))  # |or
    # # Q包裹，逗号分割还是and关系，但是现在可以换连接符了
    # res = models.Book.objects.filter(~Q(sell__gt=100) | ~Q(price__lt=200))  # ~not
    # print(res)
    #
    # # Q查询的高阶用法，能够将查询条件的左边也变成字符串形式
    # q = Q()
    # q.connector = 'or'  # 由and变成or
    # q.children.append(('sell__gt', 100))
    # q.children.append(('price', 200))
    # res = models.Book.objects.filter(q)  # 默认还是And关系，
    # print(res)

    #
    # 事务
    # from django.db import transaction
    # try:
    #     with transaction.atomic():
    #         # sql1
    #         # 在with代码块书写的所有orm操作都是属于同一个事务
    #         pass
    # except Exception as e:
    #     print(e)
    #
    # print('执行其他操作')

    # res = models.Book.objects.all()
    # print(res)  # 只有在使用数据才会走数据库

    # # 获取书籍表中所有的书的名字
    # res = models.Book.objects.values('title')
    # for d in res:
    #
    #     print(d.get('title'))
    #
    # # 获取数据对象，点title能够拿到书名，并没有其他字段
    # book_obj = models.Book.objects.only('title')
    # for i in book_obj:
    #
    #     print(i.title)
    #     print(i.price)  # 点only括号内没有的字段，会从数据库重新查询，而all()是一次型查询

    # res = models.Book.objects.defer('title')
    # for i in res:
    #     print(i.price)

    # res = models.Book.objects.all()
    # for i in res:
    #     print(i.publish.name)  # 每循环一次都要走一次数据库查询

    # # select_related
    # res = models.Book.objects.select_related('publish')
    # """
    # select_related：内部先将两个表连起来，然后一次性将大表里面的所有数据，全部封装给查询出来的对象
    #     这时候对象点任意一张表的字段都无需重新查找数据库
    # 注意事项：括号内只能放外键字段，并且多对多关系无法使用
    # """
    # for i in res:
    #     print(i.publish.name)

    # prefetch_related
    res = models.Book.objects.prefetch_related('publish')  # 子查询
    """
    子查询：将一张表的结果当作另外一张表的条件
    prefetch_related:该方法就是子查询
        将子查询查询出来的所有结果也给封装到对象中
        给你的感觉好像是一次搞点
    """
    for i in res:
        print(i.publish.name)








