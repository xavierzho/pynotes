from django.db import models
from django.contrib.auth.models import AbstractUser


# # 扩展表的方式一(不推荐)：一对一关系
# class UserDetail(models.Model):
#     phone = models.BigIntegerField()
#     user = models.OneToOneField(to='User')


# python manage.py makemigrations  # 将操作记录记录到migrations文件夹中
# python manage.py migrate
# python manage.py createsuperuser # 创建超级用户
class Users(AbstractUser):
    """
    继承AbstractUser类，行数据库迁移命令的时候不再创建auth_user表，Users表继承auth_user表所有字段，外加扩展字段
    前提：
       1.在继承之前没有执行过数据库迁移命令(auth_user表没有被创建)，"假如表已经创建，那就需要换一个数据库"
       2.继承的类里面，不要覆盖AbstractUser里面的字段名
       3.需要在配置文件中，AUTH_USER_MODEL = "users.UserInfo=应用名.表名
    """
    # 扩展字段
    phone = models.CharField(max_length=20, verbose_name='用户的电话号码', null=True)
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.jpg', verbose_name='用户的头像')
    desc = models.CharField(max_length=64, verbose_name='个人简介', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的创建时间')
    self_site = models.CharField(max_length=32, verbose_name='个人网站名')
    # self_site = models.OneToOneField(to="SelfSite", null=True, on_delete=models.CASCADE, verbose_name='个人网站的id')
    # on_delete=models.CASCADE 2.0版本以上必须定义，是否级联更新级联删除
    """
    CharField 不指定max_length参数会报错
    """

    class Meta:
        verbose_name_plural = '用户表'  # 修改admin后台管理默认的表名
        verbose_name = '用户表'  # 末尾会自动加S


class PersonalInfo(models.Model):
    # orm会自动创建主键字段名为id，无特殊需求无需改变
    name = models.CharField(max_length=32, verbose_name='真实名字', null=True)
    gender_choices = (
        ('1', '男'),
        ('2', '女'),
        ('3', '其他'),
    )
    # 保证字段类型跟列举出来的元组第一个数据类型一致即可
    gender = models.CharField(choices=gender_choices, max_length=1, verbose_name='性别', null=True)
    born = models.DateField(verbose_name='出生年月日', null=True)
    hometown = models.CharField(max_length=64, verbose_name='家乡', null=True)
    location = models.CharField(max_length=64, verbose_name='当前所在城市', null=True)
    marriage_choices = (
        ('1', '单身'),
        ('2', '热恋中'),
        ('3', '订婚'),
        ('4', '已婚'),
        ('5', '离异'),
    )
    marriage = models.CharField(choices=marriage_choices, max_length=1, verbose_name='婚姻状况', null=True)
    position = models.CharField(max_length=64, verbose_name='职位')
    company = models.CharField(max_length=64, verbose_name='公司')
    work_condition_choices = (
        ('1', '学生'),
        ('2', '已工作'),
        ('3', '待业中'),
        ('4', '其他'),
    )
    work_situation = models.CharField(choices=work_condition_choices, max_length=1, verbose_name='工作状况')
    # 一对一字段，对应Users表
    user = models.OneToOneField(to='Users', on_delete=models.CASCADE, verbose_name='用户id')

    def __str__(self):
        # admin后台管理中打印的字符串
        return "%s" % self.name
