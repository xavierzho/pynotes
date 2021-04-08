from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from main import views
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('order/', views.Order.as_view()),
    path('user/', views.UserInfoView.as_view()),
    path('goods/', views.GoodsInfoAPIView.as_view()),
    path('login2/', views.Login2View.as_view(actions={'post': 'login'})),

]
