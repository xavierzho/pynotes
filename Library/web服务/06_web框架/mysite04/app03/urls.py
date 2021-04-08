from django.conf.urls import url
from app03 import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.home, name='app03_home'),
    url(r'^index/', views.index, name='app03_index'),
    url(r'^csrf/', views.MyCsrfToken.as_view(), name='app03_csrf')
]
