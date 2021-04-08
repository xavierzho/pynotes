import re
import random
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from . import models


class IssueToken:
    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(phone=username).first()
        elif re.match('^.*@.*\..*', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()

        if user:
            ret = user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    def _issue_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class LoginSerializer(serializers.ModelSerializer, IssueToken):
    # 多方式登录，可能username存在，无法反序列
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ('username', 'password', 'id')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
            'id': {'read_only': True}
        }

    def validate(self, attrs):
        user_obj = self._get_user(attrs)
        token = self._issue_token(user_obj)
        self.context['token'] = token
        self.context['user'] = user_obj
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(min_length=6, max_length=6)

    class Meta:
        model = models.User
        fields = ('phone', 'password', 'code')

    def validate(self, attrs):
        phone = attrs.get('phone')
        code = attrs.get('code')
        username = 'JX'
        for _ in range(8):
            username += str(random.randint(0, 9))
        if code == '199706':
            if re.match("^1[3-9][0-9]{9}", phone):
                attrs['username'] = username
                attrs.pop('code')
            else:
                raise ValidationError('非法手机号')
        else:
            raise ValidationError('验证码错误')

    def create(self, validated_data):
        # 验证正确
        user = models.User.objects.create_user(**validated_data)
        return user
