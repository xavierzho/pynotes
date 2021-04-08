import jwt
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler
from main import models


class CookieAuthentication(BaseJSONWebTokenAuthentication):
    """自定义JWT认证，从cookie中获取认证信息"""

    def get_jwt_value(self, request):
        # print request.COOKIES
        print(request.COOKIES)
        return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE.upper(), '')

    def authenticate(self, request):
        jwt_value = self.get_jwt_value(request)
        if not jwt_value:
            raise exceptions.AuthenticationFailed('cookies中没有信息，或者过期了')
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed('签名过期')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('非法用户')
        print(payload.get('username'))
        user = models.Users.objects.filter(username=payload.get('username')).first()
        print(user)

        return user, jwt_value
