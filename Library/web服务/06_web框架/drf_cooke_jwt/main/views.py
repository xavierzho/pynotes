from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from main import models
from main import ser
from main import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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


class Register(CreateModelMixin, GenericViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = models.Users.objects.all()
    serializer_class = ser.RegisterModelSerializer



def index(request):

    response = render(request, 'index.html')
    return response
