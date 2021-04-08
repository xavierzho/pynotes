"""MyBlog URL Configuration

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
from django.views.static import serve
from MyBlog import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='main_home'),
    path('login/', views.login, name='main_login'),
    path('reg/', views.reg, name='main_reg'),
    path('writer/', views.writer, name='main_writer'),
    path('settings/reset_pwd/', views.reset_password, name='main_reset_pwd'),
    path('get_code/', views.get_code, name='main_get_code'),
    path('logout/', views.logout, name='main_logout'),
    path('settings/account/', views.account_settings, name='main_account_setting'),
    path('settings/profile', views.profile_settings, name='main_profile_setting'),
    path('settings/others', views.other_settings, name='main_other_setting'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

]
