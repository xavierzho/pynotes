from rest_framework import serializers, exceptions
from api import models


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
