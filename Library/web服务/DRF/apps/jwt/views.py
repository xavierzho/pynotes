import time
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from apps.jwt import models
from apps.jwt.utils import ser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from apps.jwt.utils.jwt_auth import JWTAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from utils.serializer import UserSerializer, AvatarSerializer, UserReadOnlySerializer, LoginModelSerializer


class ChangePassword(UpdateModelMixin, GenericViewSet):
    queryset = models.Users.objects.all()
    serializer_class = ser.ChangePasswordModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]


class Login(ViewSet):
    authentication_classes = []
    permission_classes = []

    def login(self, request, *args, **kwargs):  # 不写post写login

        # 1.需要序列化类
        login_ser = ser.LoginModelSerializer(data=request.data, context={'request': request})
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
        }, content_type='application/json')


# class Register(CreateModelMixin, GenericViewSet):
#     permission_classes = []
#     authentication_classes = []
#     queryset = models.Users.objects.all()
#     serializer_class = ser.RegisterModelSerializer


def index(request):
    response = render(request, 'index.html')
    return response


class BookView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        print(request.user.email)
        return Response('ok')


class Register(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = models.Users.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [MultiPartParser]

    def get_serializer_class(self):
        print(self.action)

        if self.action == 'create':
            return UserSerializer
        elif self.action == 'retrieve':
            return UserReadOnlySerializer
        elif self.action == 'update':
            return AvatarSerializer


# @cache_page(15)
def test_cache(request):
    cache.set('name', 'jones')

    ctime = time.time()
    return render(request, 'test.html', locals())


def test_cache2(request):
    name = cache.get('name')
    print(name)
    return render(request, 'test.html', locals())


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
