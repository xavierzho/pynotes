from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Book
# from main.ser import BookModelSerializer
from main.ser import BookSerializer, BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from main.untils import Message
from rest_framework.request import Request
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import BrowsableAPIRenderer


class BookView(APIView):
    def get(self, request, pk):
        book_obj = Book.objects.filter(nid=pk).first()
        # 序列化谁把谁传过来
        book_ser = BookSerializer(book_obj)
        # 就是序列化后的字典
        # return JsonResponse(book_ser.data)
        return Response(book_ser.data)

    def put(self, request, pk):
        response_msg = {'status': 200, 'msg': 'OK'}
        # 找到要修改的对象
        book_obj = Book.objects.filter(nid=pk).first()
        # 得到一个序列化类的对象,用request.data来修改这个对象
        # book_ser = BookSerializer(book_obj, request.data)
        book_ser = BookSerializer(instance=book_obj, data=request.data)
        # 要数据验证
        if book_ser.is_valid():
            # 表示验证通过，进行保存操作
            book_ser.save()
            # 返回序列化验证过后的数据
            response_msg['data'] = book_ser.data
            return Response(response_msg)
        else:
            response_msg['status'] = 101
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
            return Response(response_msg)

    def delete(self, request, pk):
        response_msg = Message()
        res = Book.objects.filter(pk=pk).delete()
        response_msg.data = res
        return Response(response_msg)


class BooksView(APIView):
    def get(self, request):
        response_msg = {'status': 200, 'msg': 'OK'}
        books = Book.objects.all()
        book_ser = BookSerializer(books, many=True)  # 序列化多条，需要加上many=True
        response_msg['data'] = book_ser.data
        return Response(response_msg)

    def post(self, request):
        response_msg = {'status': 200, 'msg': 'OK'}

        book_ser = BookSerializer(data=request.data, many=True)  # 序列化多条，需要加上many=True
        # 校验字段
        if book_ser.is_valid():
            book_ser.save()
            response_msg['data'] = book_ser.data
        else:
            response_msg['status'] = 102
            response_msg['msg'] = '数据校验失败'
            response_msg['data'] = book_ser.errors
        return Response(response_msg)


class BooksView2(APIView):
    def get(self, request):
        response_msg = {'status': 200, 'msg': 'OK'}
        books = Book.objects.all()
        book = Book.objects.all().first()
        books_ser = BookModelSerializer(books, many=True)
        book_ser = BookModelSerializer(book)
        print(type(book_ser), type(books_ser))
        response_msg['data'] = book_ser.data
        return Response(response_msg)


class TextView(APIView):
    def get(self, request):
        renderer_classes = [JSONRenderer, ]
        print(request)
        return Response({'name': 'jones'}, status=status.HTTP_200_OK, headers={'token': 'xxx'})


class TextView2(APIView):
    def get(self, request):
        print(request)
        return Response({'name': 'jones'}, status=status.HTTP_200_OK, headers={'token': 'xxx'})
