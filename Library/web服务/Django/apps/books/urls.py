"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path
from . import views


urlpatterns = [
    # 首页
    path(r'/', views.home, name='books_home'),
    # 图书展示页
    path('list/', views.book_list, name='books_list'),
    # 书籍的添加
    path('add/', views.book_add, name='books_add'),
    # 书籍的编辑
    path('edit/<edit:int>', views.book_edit, name='books_edit'),
    # 书籍的删除
    path('delete/(<del_id:int>', views.book_del, name='books_del'),
    # 分页器使用
    path("pager/", views.botch())
]