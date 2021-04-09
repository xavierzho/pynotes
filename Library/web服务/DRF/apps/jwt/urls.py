"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken, RefreshJSONWebToken, obtain_jwt_token, \
    verify_jwt_token, refresh_jwt_token
from django.views.static import serve
from django.conf import settings
from apps.jwt import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('register', views.Register, 'register')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('login/', views.Login.as_view(actions={'post': 'login'})),
    path('register/', views.Register.as_view(actions={'post': 'create'})),
    path('reset_password/', views.ChangePassword.as_view(actions={'put': 'update'})),
    path('test/', views.index),


    # path('register/', views.Register.as_view(actions={'post': 'create'}))
    path('', include(router.urls)),  # 第二种方式
    # cache
    path('test/', views.test_cache),
    path('test2/', views.test_cache2),
    # jwt
    path('books/', views.BookView.as_view()),
    path('login/', obtain_jwt_token),
    path('order/', views.Order.as_view()),
    path('user/', views.UserInfoView.as_view()),
    path('goods/', views.GoodsInfoAPIView.as_view()),
    path('login2/', views.Login2View.as_view(actions={'post': 'login'})),

]

# urlpatterns += router.urls  # 一种方式