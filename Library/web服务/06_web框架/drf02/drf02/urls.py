"""drf02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
# 1.导包
from rest_framework import routers

# 2.实例化类，SimpleRouter或DefaultRouter
router = routers.DefaultRouter()
# 3.注册,router.register('前缀', '继承自ModelViewSet的视图类', 别名)
router.register('books7', views.Book7View)
# 4.自动生成路由
print(router.urls)
# [<URLPattern '^books7/$' [name='book-list']>, <URLPattern '^books7/(?P<pk>[^/.]+)/$' [name='book-detail']>]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', views.BookView.as_view()),
    path('api/books/<int:pk>/', views.BookDetailView.as_view()),
    # 使用GenericAPIView重写
    path('api/books2/', views.BookGenericView.as_view()),
    path('api/books2/<int:pk>/', views.BookGenericDetailView.as_view()),
    # 基于GenericAPIView封装的方法
    path('api/books3/', views.Book3View.as_view()),
    path('api/books3/<int:pk>/', views.Book3DetailView.as_view()),
    # 基于GenericAPIView的9个子类
    path('api/books4/', views.Book4View.as_view()),
    path('api/books4/<int:pk>/', views.Book4DetailView.as_view()),
    # 使用ModelViewSet写的5个接口
    path('api/books5/', views.Book5View.as_view(actions={'get': 'list', 'post': 'create'})),
    path('api/books5/<int:pk>/',
         views.Book5View.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 继承ViewSetMixin路由可以改写
    path('api/books6/', views.Book6View.as_view(actions={'get': 'get_all_book'})),
    # path('api/books7/', views.Book7View.as_view(actions={'get': 'list', 'post': 'create'})),
    # path('api/books7/<int:pk>/', views.Book7View.as_view(
    # actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),


]

# 5.添加到路由匹配列表中取
urlpatterns += router.urls
