"""BBS URL Configuration

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
from django.urls import path, re_path
from app01 import views
from django.views.static import serve
from BBS import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', views.register, name='app01_reg'),
    path('login/', views.login, name='app01_login'),
    path('get_code/', views.get_code, name='app01_get_code'),
    path('', views.home, name='app01_home'),
    # 编辑器上传图片接口
    path('upload_img/', views.upload_img),
    # 点赞点踩
    path('up_or_down/', views.up_or_down),
    # 文章评论
    path('comment/', views.comment),
    path('writer/', views.writer, name='app01_writer'),
    path('logout/', views.logout, name='app01_logout'),
    path('reset_pwd/', views.reset_password, name='app01_reset_pwd'),
    # 暴露后端指定文件夹资源
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^(?P<username>\w+)/$', views.site, name='app01_site'),
    # 多个url同一个视图函数
    # re_path(r'^(?P<username>\w+)/category/(\d+)/', views.site),
    # re_path(r'^(?P<username>\w+)/tag/(\d+)/', views.site),
    # re_path(r'^(?P<username>\w+)/archive/(\w+)/', views.site),
    # 上面的url可以合并成一条
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)', views.site),

    # 文章详情页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)', views.article_detail, name='app01_article_detail'),

]
