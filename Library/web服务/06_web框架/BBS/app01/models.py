from django.db import models
from django.contrib.auth.models import AbstractUser
import os


# Create your models here.


class Users(AbstractUser):
    phone = models.BigIntegerField(verbose_name='用户的电话号码', null=True)
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.jpg', verbose_name='用户的头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的创建时间')
    self_site = models.OneToOneField(to='SelfSite', null=True, on_delete=models.CASCADE, verbose_name='个人网站的id')

    class Meta:
        verbose_name_plural = '用户表'  # 修改admin后台管理默认的表名
        verbose_name = '用户表'  # 末尾会自动加S


class SelfSite(models.Model):
    name = models.CharField(max_length=32, verbose_name='个人网站名称')
    title = models.CharField(max_length=32, verbose_name='个人网站标题')

    theme = models.FilePathField(path=os.path.join(os.path.dirname(__file__), 'site_theme'),
                                 verbose_name='个人网站的样式，存css/js文件路径')

    class Meta:
        verbose_name_plural = '个人站点表'

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=32, verbose_name='文章标签名')
    self_site = models.ForeignKey(to='SelfSite', null=True, on_delete=models.CASCADE, verbose_name='个人网站的id值')

    class Meta:
        verbose_name_plural = '标签表'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='文章分类名')
    self_site = models.ForeignKey(to='SelfSite', null=True, on_delete=models.CASCADE, verbose_name='个人网站的id值')

    class Meta:
        verbose_name_plural = '分类表'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    desc = models.CharField(max_length=256, verbose_name='文章摘要')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    content = models.TextField(verbose_name='文章内容')
    up_num = models.BigIntegerField(verbose_name='点赞数', default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数', default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数', default=0)
    self_site = models.ForeignKey(to='SelfSite', on_delete=models.CASCADE, verbose_name='个人网站的id值')
    article_tag = models.ManyToManyField(to='Tags', through='Article2Tag', through_fields=('article', 'tag'),
                                         verbose_name='文章标签id值')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='文章分类的id值')

    class Meta:
        verbose_name_plural = '文章表'

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tags', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '文章和标签关系表'


class UpOrDown(models.Model):
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户的id值')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='文章的id值')
    is_up = models.BooleanField()

    class Meta:
        verbose_name_plural = '点赞点踩表'

    def __str__(self):
        return self.user


class ArticleComment(models.Model):
    user = models.ForeignKey(to='Users', on_delete=models.CASCADE, verbose_name='用户的id值')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='文章的id值')
    content = models.CharField(max_length=256, verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, verbose_name='子评论')

    class Meta:
        verbose_name_plural = '评论表'

    def __str__(self):
        return self.user
