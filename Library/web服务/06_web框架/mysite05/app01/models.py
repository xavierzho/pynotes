from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


# # 扩展表的方式一(不推荐)：一对一关系
# class UserDetail(models.Model):
#     phone = models.BigIntegerField()
#     user = models.OneToOneField(to='User')


# 扩展表的方式二：面向对象的继承
class UserInfo(AbstractUser):
    """
    如果继承了AbstractUser类，在执行数据库迁移命令的时候，auth_user表就不会在创建出来了
    而UserInfo表中会出现auth_user表中所有的字段，外加扩展的字段
    这么做的好处在于能够直接点击你自己的表，更加快速的完成操作及扩展
    
    前提：
       1.在继承之前没有执行过数据库迁移命令(auth_user表没有被创建)
            假如表已经创建，那就需要换一个数据库
       2.继承的类里面，不要覆盖AbstractUser里面的字段名
       3.需要在配置文件中，告诉django你要使用UserInfo表替换auth_user表
            AUTH_USER_MODEL = "app01.UserInfo"
                                应用名.表名
    """
    phone = models.BigIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
