import re
from rest_framework import serializers, exceptions
from apps.jwt import models
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


class UserSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField()

    def get_password(self, instance):
        return "***"

    # 因为confirm_password没有，所以需要定义
    confirm_password = serializers.CharField(max_length=16, min_length=8, required=True, write_only=True)

    class Meta:
        model = models.Users

        fields = ('username', 'password', 'phone', 'confirm_password', 'avatar')
        extra_kwargs = {
            'username': {'max_length': 16, 'min_length': 4, 'required': True},
            'password': {'max_length': 16, 'min_length': 8, 'required': True, 'write_only': True},

        }

    def validated_phone(self, data):
        if not len(data) == 11:
            raise exceptions.ValidationError('手机号码不合法')
        return data

    def validate(self, attrs):
        if not attrs.get('password') == attrs.get('confirm_password'):
            raise exceptions.ValidationError('两次密码不相同')
        else:
            attrs.pop('confirm_password')  # 剔除该字段，数据库没有该字段
        return attrs

    def create(self, validated_data):
        user = models.Users.objects.create_user(**validated_data)
        return user


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users

        fields = ('avatar',)


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users

        fields = ('username', 'avatar')


class LoginModelSerializer(serializers.ModelSerializer):
    # 这里需要覆盖掉username字段，因为在数据库中，他是unique=True,post会认为想要保存数据，自己校验不通过
    username = serializers.CharField()

    class Meta:
        model = models.Users
        fields = ('username', 'password')

    def validate(self, attrs):
        # 视图传过来的数据
        # print(self.context)
        # 在这写逻辑
        username = attrs.get('username')
        password = attrs.get('password')
        # 通过判断数据不同，username不同，查询的字段不一样
        # 通过正则匹配

        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.Users.objects.filter(phone=username).first()
        elif re.match('^.*@.*$', username):
            user = models.Users.objects.filter(email=username).first()
        else:
            user = models.Users.objects.filter(username=username).first()
        if user:
            # 校验密码,密文密码需要用check_password
            if user.check_password(password):
                # 签发token
                payload = jwt_payload_handler(user)
                # print(payload)
                token = jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username'] = user.username
                self.context['exp'] = payload.get('exp')

                return attrs
            else:
                raise exceptions.ValidationError('密码错误')
        else:
            raise exceptions.ValidationError('用户不存在')
