import time
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from utils.jwt_auth import JWTAuthentication
from api import models
from utils.serializer import UserSerializer, AvatarSerializer, UserReadOnlySerializer
from django.views.decorators.cache import cache_page
from django.core.cache import cache


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