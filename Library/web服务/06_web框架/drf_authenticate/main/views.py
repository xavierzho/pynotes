import uuid
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.throttling import AnonRateThrottle
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from main import models
from main.utils.serializer import BookSerializer, Book2Serializer
from main.utils.auth_class import UserAuthenticate
from permissions.utils.auth_permission import UserPermission
from main.utils.response import APIResponse


# Create your views here.


class BookView(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [UserAuthenticate]

    @action(methods=['get', 'post'], detail=True)
    def get_2(self, request, pk):
        print(request.user.username)
        print(pk)
        book = self.queryset[:2]
        ser = self.serializer_class(book, many=True)
        return Response(ser.data)


class Login(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.Users.objects.filter(username=username, password=password).first()
        if user:
            # 登录成功,生成一个随机字符串
            token = uuid.uuid4()
            # 存到userToken表中
            # models.UserToken.objects.create(token=token, user=user)  # 用它每次登录都会记录一条
            models.UserToken.objects.update_or_create(defaults={'token': token}, user=user)  # 有则更新无则新增

            return Response({'status': 200, 'msg': "login success", 'token': token})
        else:
            return Response({'status': 201, 'msg': '用户名或密码错误'})


class TestView(APIView):
    permission_classes = [UserPermission]

    def get(self, request, *args, **kwargs):
        return Response('这是个测试')


# 演示内置权限
class TestSuperUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        print(request.user.is_staff)
        return Response('超级管理员用户才能看')


# 匿名用户访问频次全局使用
class TestAnonUser(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print(request.META)
        return Response('访问频次限制，全局配置')


# 匿名用户访问频次局部使用
class TestAnonUser2(APIView):
    authentication_classes = [UserAuthenticate]
    permission_classes = []
    throttle_classes = [AnonRateThrottle]

    def get(self, request, *args, **kwargs):
        # 1/0
        print(request.META)
        return Response('访问频次限制，局部配置')


# 登录用户访问频次全局使用
class TestLoginUser(APIView):
    authentication_classes = [SessionAuthentication]

    # permission_classes = []
    # throttle_classes = [AnonRateThrottle]

    def get(self, request, *args, **kwargs):
        print(request.META)
        return Response('访问频次限制，局部配置')


class TestFilter(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('name', 'publish')


# 排序组件的使用
class TestOrdering(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('id', 'price')


# 自定义Response对象
class TestView8(APIView):
    def get(self, request, *args, **kwargs):
        return APIResponse(data={'name': 'jones'}, token='qwioasjioqwehjtroq',
                           headers={'token': 'jones is the best progring'})


class TestView9(GenericAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        book = self.get_queryset()

        ser = self.serializer_class(data=book, many=True)
        return APIResponse(data=ser.data)

    def post(self, request, *args, **kwargs):

        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            ser.save()

