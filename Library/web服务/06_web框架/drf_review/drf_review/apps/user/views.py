import re
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ViewSet
from drf_review.utils.response import APIResponse
from . import models, serializer


class LoginView(ViewSet):

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        # print(request.data)
        ser = serializer.LoginSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(data={'username': username, 'token': token})
        else:
            return APIResponse(code=0, msg=ser.errors)

    @action(methods=['get'], detail=False)
    def check_phone(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        if not re.match('^1[3-9][0-9]{9}', phone):
            return APIResponse(code=0, msg='非法手机号')
        try:
            models.User.objects.get(phone=phone)
            return APIResponse(msg='该手机号已经注册')
        except Exception as e:

            return APIResponse(msg='该手机号可以注册')


class SendSMS(ViewSet):

    @action(methods=['post'], detail=False)
    def send_code(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        if not re.match('^1[3-9][0-9]{9}', phone):
            return APIResponse(msg='非法手机号')
        return APIResponse('发送成功')


class Register(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = response.data.get('username')
        return APIResponse(msg='注册成功', username=username)
