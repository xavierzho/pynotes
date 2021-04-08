"""drf_jwt URL Configuration

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
from django.urls import path, include
from api import views
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken, RefreshJSONWebToken, obtain_jwt_token, \
    verify_jwt_token, refresh_jwt_token
# 基类JSONWebTokenAPIView继承了APIView
# ObtainJSONWebToken, VerifyJSONWebToken, RefreshJSONWebToken继承了JSONWebTokenAPIView
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# verify_jwt_token = VerifyJSONWebToken.as_view()
from rest_framework.routers import SimpleRouter
from django.views.static import serve
from django.conf import settings
router = SimpleRouter()
router.register('register', views.Register, 'register')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', ObtainJSONWebToken.as_view())
    path('login/', obtain_jwt_token),
    path('books/', views.BookView.as_view()),
    path('api/', include('api.urls')),
    # path('register/', views.Register.as_view(actions={'post': 'create'}))
    path('', include(router.urls)),  # 第二种方式
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('main/', include('main.urls')),

]
# urlpatterns += router.urls  # 一种方式
