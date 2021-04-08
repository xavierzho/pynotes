from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='用户的电话号码', null=True)
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.jpg', verbose_name='用户的头像')
    desc = models.CharField(max_length=64, verbose_name='个人简介', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的创建时间')
    self_site = models.CharField(max_length=32, verbose_name='个人网站名')


class PersonalInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='真实名字', null=True)
    gender_choices = (
        ('1', '男'),
        ('2', '女'),
        ('3', '其他'),
    )
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
    user = models.OneToOneField(to='Users', on_delete=models.CASCADE, verbose_name='用户id')


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='文章分类名')
    desc = models.CharField(max_length=128, verbose_name='分类描述')
    is_allow_submit = models.BooleanField(verbose_name='是否允许投稿')
    submit_check = models.BooleanField(verbose_name='投稿是否需要审核')
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户id')


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    desc = models.CharField(max_length=256, verbose_name='文章摘要')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    content = models.TextField(verbose_name='文章内容')
    up_num = models.BigIntegerField(verbose_name='点赞数', default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数', default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数', default=0)
    article_tag = models.ManyToManyField(to='Tags', through='Article2Tag', through_fields=('article', 'tag'), verbose_name='文章标签id值')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='文章分类的id值')
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE)


class Tags(models.Model):
    name = models.CharField(max_length=64, verbose_name='标签名')
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户的id值')


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tags', on_delete=models.CASCADE)


class UpOrDown(models.Model):
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户的id值')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='文章的id值')
    is_up = models.BooleanField()


class ArticleComment(models.Model):
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户的id值')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='文章的id值')
    content = models.CharField(max_length=256, verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, verbose_name='子评论')


class Likes(models.Model):
    user = models.OneToOneField(to='Users', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)


class Favorites(models.Model):
    user = models.OneToOneField(to='Users', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)

