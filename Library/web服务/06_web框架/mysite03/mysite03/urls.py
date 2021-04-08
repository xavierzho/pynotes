"""mysite03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from app01 import urls as app01_urls
# from app02 import urls as app02_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 路由分发
    # url(r'^app01/', include(app01_urls)),  # 只要是app01前缀开头的，全部交给app01处理
    # url(r'^app02/', include(app02_urls)),  # 只要是app02前缀开头的，全部交给app02处理
    # 终极写法：不用导包
    # url(r'^app01/', include('app01.urls', namespace='app01')),
    # url(r'^app02/', include('app02.urls', namespace='app02')),
    # 不使用名称空间
    url(r'^app01/', include('app01.urls')),
    url(r'^app02/', include('app02.urls')),
    url(r'^app03/', include('app03.urls')),
]
