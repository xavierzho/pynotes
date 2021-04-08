from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ajax相关
    url(r'^ab_ajax/', views.ab_ajax),
    # 前后端传输数据格式研究
    url(r'^index/', views.index),
    # ajax发送json格式数据
    url(r'^send_json/', views.send_json),
    # ajax发送文件
    url(r'^send_file/', views.send_file),
    # 序列化组件
    url(r'^ab_ser/', views.ab_ser),
    # 批量插入数据
    url(r'^botch/', views.botch),
    # form组件前序注册功能
    url(r'^reg/', views.reg),
    # forms组件渲染标签
    url(r'^verify/', views.render_tag),
]