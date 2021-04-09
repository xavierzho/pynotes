from .utils.auth_permission import UserPermission
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class BookView(APIView):
    permission_classes = [UserPermission]
    authentication_classes = []

    def get(self, request):
        print(request)
        return Response('这是个测试')
