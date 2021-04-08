import jwt
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import get_authorization_header, jwt_get_username_from_payload
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_encode_handler, jwt_decode_handler


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        # 取出token
        jwt_value = str(request.META.get("HTTP_AUTHORIZATION"))
        # 认证
        try:
            payload = jwt_decode_handler(jwt_value)
            print(payload)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise AuthenticationFailed()

        user = self.authenticate_credentials(payload)
        return user, None


