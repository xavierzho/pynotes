from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from main.utils import JWTAuthentication
from django.http.response import JsonResponse
from main.ser import LoginModelSerializer


class Order(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    # 权限类
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response('这是订单信息')


class UserInfoView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]

    # 权限类
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response('UserInfo')


class GoodsInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response('商品信息')


# class Login2View(ViewSetMixin, APIView):
class Login2View(ViewSet):  # 和上面完全一样

    def login(self, request, *args, **kwargs):  # 不写post写login

        # 1.需要序列化类
        login_ser = LoginModelSerializer(data=request.data, context={'request': request})
        # 2.生成序列化对象
        # 3.调用序列化对象的is_valid
        login_ser.is_valid(raise_exception=True)
        token = login_ser.context.get('token')

        # 4.返回
        return Response({
            'status': 200,
            'msg': '登录成功',
            'username': login_ser.context.get('username'),
            'token': token
        })

