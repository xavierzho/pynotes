from django.conf.urls import url
from django.contrib import admin
from app03 import views


urlpatterns = [
    # 首页
    url(r'^$', views.home, name='app03_home'),
    # 图书展示页
    url(r'^book/list/', views.book_list, name='app03_booklist'),
    # 书籍的添加
    url(r'^book/add/', views.book_add, name='app03_add'),
    # 书籍的编辑
    url(r'^book/edit/(?P<edit_id>\d+)', views.book_edit, name='app03_edit'),
    # 书籍的删除
    url(r'^book/delete/(?P<del_id>\d+)', views.book_del, name='app03_del')
]