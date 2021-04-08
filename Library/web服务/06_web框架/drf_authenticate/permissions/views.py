from django.shortcuts import render
from permissions.utils.auth_permission import UserPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.


class BookView(APIView):
    permission_classes = [UserPermission]
    authentication_classes = []

    def get(self, request):
        print(request)
        return Response('这是个测试')
