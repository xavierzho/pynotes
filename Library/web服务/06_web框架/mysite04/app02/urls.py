from django.conf.urls import url
from django.contrib import admin
from app02 import views

urlpatterns = [
    url(r'^$', views.home, name='app02_home'),
    url(r'^login/', views.login, name='app02_login'),
    url(r'^index/', views.index, name='app02_index'),
    url(r'^func/', views.func, name='app02_func'),
    url(r'^logout/', views.logout, name='app02_logout'),
    # session
    url(r'^set_session', views.set_session, name='app02_set_session'),
    url(r'^get_session', views.get_session, name='app02_get_session'),
    url(r'^del_session', views.del_session, name='app02_get_session'),
    url(r'^mylogin', views.MyLogin.as_view(), name='app02_my_login')
]