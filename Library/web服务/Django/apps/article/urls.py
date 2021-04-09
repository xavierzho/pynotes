"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path,re_path
from apps.article import views

urlpatterns = [
    # 编辑器上传图片接口
    path('upload_img/', views.upload_img),
    # 点赞点踩
    path('up_or_down/', views.up_or_down, name="article_up"),
    # 文章评论
    path('comment/', views.comment,name="article_comment"),
    re_path(r'^(?P<username>\w+)/$', views.site, name='article_site'),
    # 多个url同一个视图函数
    # re_path(r'^(?P<username>\w+)/category/(\d+)/', views.site),
    # re_path(r'^(?P<username>\w+)/tag/(\d+)/', views.site),
    # re_path(r'^(?P<username>\w+)/archive/(\w+)/', views.site),
    # 上面的url可以合并成一条
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)', views.site),
    # 文章详情页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)', views.article_detail, name='article_detail'),
]
