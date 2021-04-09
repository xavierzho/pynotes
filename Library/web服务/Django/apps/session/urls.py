"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_session, name='session_set'),
    path('get/', views.get_session, name='session_get'),
    path('del/', views.del_session, name='session_del'),
    path('mylogin/', views.MyLogin.as_view(), name='session_login'),
    path(r'csrf/', views.MyCsrfToken.as_view(), name='session_csrf'),

]