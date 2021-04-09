"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""

from django.urls import path
from . import views
# 1.导包
from rest_framework import routers

# 2.实例化类，SimpleRouter或DefaultRouter
router = routers.DefaultRouter()
# 3.注册,router.register('前缀', '继承自ModelViewSet的视图类', 别名)
router.register('books7', views.BooksModelViewSet)
# 4.自动生成路由
print(router.urls)
# [<URLPattern '^books7/$' [name='book-list']>, <URLPattern '^books7/(?P<pk>[^/.]+)/$' [name='book-detail']>]

urlpatterns = [

    path('books/<int:pk>', views.BookView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('books2/', views.BooksViewByModelSer.as_view()),
    # restful
    path('api/books/', views.BookView.as_view()),
    path('api/books/<int:pk>/', views.BookDetailView.as_view()),
    # 使用GenericAPIView重写
    path('api/books2/', views.BookGenericAPIView.as_view()),
    path('api/books2/<int:pk>/', views.BookGenericDetailView.as_view()),
    # 基于GenericAPIView封装的方法
    path('api/books3/', views.BookGenericView.as_view()),
    path('api/books3/<int:pk>/', views.BookGenericAPIDetailView.as_view()),
    # 基于GenericAPIView的9个子类
    path('api/books4/', views.BookListCreateAPIView.as_view()),
    path('api/books4/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
    # 使用ModelViewSet写的5个接口
    path('api/books5/', views.BookModelViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('api/books5/<int:pk>/',
         views.BookModelViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 继承ViewSetMixin路由可以改写
    path('api/books6/', views.BookGenericViewSet.as_view(actions={'get': 'get_all_book'})),
    # path('api/books7/', views.Book7View.as_view(actions={'get': 'list', 'post': 'create'})),
    # path('api/books7/<int:pk>/', views.Book7View.as_view(
    # actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

# 5.添加到路由匹配列表中取
urlpatterns += router.urls
