from django.conf.urls import url
from django.contrib import admin
from app01 import views


urlpatterns = [
    # 首页
    url(r'^$', views.home),
    # 登录页(查询)
    url(r'^login/', views.login),
    # 注册页(增加)
    url(r'^reg/', views.register, name='app01_reg'),
    # 无名分组的反向解析
    url(r'^index/(\d+)/', views.index, name='app01_xxx'),
    # 有名分组的方向解析
    url(r'^func/(?P<year>\d+)/', views.func, name='app01_ooo'),
    # 用户列表
    url(r'^user list/', views.user_list),
    # 修改
    url(r'^edit/(?P<modify>\d+)/', views.edit, name='app01_edit'),
    # 删除
    url(r'^del/(\d+)/', views.delete, name='app01_del'),
]
