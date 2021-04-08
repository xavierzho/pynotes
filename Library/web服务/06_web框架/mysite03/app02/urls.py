from django.conf.urls import url
from django.contrib import admin
from app02 import views


urlpatterns = [
    url(r'^reg.html', views.reg, name='app02_reg'),
    # 视图层三板斧
    # url(r'^index/', views.index),
    # json相关
    url(r'^ab_json', views.ab_json),
    # 上传文件
    url(r'^ab_file', views.ab_file),
    # CBV路由
    url(r'^login/', views.MyLogin.as_view()),
    # 上述代码在启动django的时候，就会立刻执行as_view()方法
    # url(r'^login/', views.view)  # 本质上还是FBV
    url(r'^index/', views.MyIndex.as_view()),
    # 模板的继承
    url(r'^home/', views.home),
    url(r'^reg/', views.reg)
]
