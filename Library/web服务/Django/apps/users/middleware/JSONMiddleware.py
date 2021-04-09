from django.utils.deprecation import MiddlewareMixin
import json


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.data = json.loads(request.body)

        except:
            request.data = request.POST
