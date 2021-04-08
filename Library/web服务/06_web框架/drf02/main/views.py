from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from main.models import Book, Publish
from main.ser import BookSerializer, PublishSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSetMixin
from rest_framework.decorators import action


# 基于APIView
class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)

    def post(self, request):
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
        book_ser = BookSerializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        book = Book.objects.all().filter(pk=pk).first()

        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})

    def delete(self, request, pk):
        res = Book.objects.filter(pk=pk).delete()
        return Response({'status': status.HTTP_200_OK, 'msg': '删除成功', 'data': res})


# 基于GenericAPIView
class BookGenericView(GenericAPIView):
    # queryset传如queryset对象
    # queryset = Book.objects
    queryset = Book.objects.all()
    # 使用哪个序列化类来序列化这些数据
    serializer_class = BookSerializer

    def get(self, request):
        book_list = self.get_queryset()
        book_ser = self.get_serializer(book_list, many=True)
        return Response(book_ser.data)

    def post(self, request):
        book_ser = self.get_serializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})


class BookGenericDetailView(GenericAPIView):
    # queryset传如queryset对象
    # queryset = Book.objects
    queryset = Book.objects.all()
    # 使用哪个序列化类来序列化这些数据
    serializer_class = BookSerializer

    def get(self, request, pk):
        book = self.get_object()
        book_ser = self.get_serializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        book = self.get_object(pk=pk)

        book_ser = self.get_serializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})

    def delete(self, request, pk):
        res = self.get_object().delete()
        return Response({'status': status.HTTP_200_OK, 'msg': '删除成功', 'data': res})


# 基于GenericAPIView写的Publish的序列化器
class PublishGenericView(GenericAPIView):
    # queryset传如queryset对象
    # queryset = Book.objects
    queryset = Publish.objects.all()
    # 使用哪个序列化类来序列化这些数据
    serializer_class = PublishSerializer

    def get(self, request):
        book_list = self.get_queryset()
        book_ser = self.get_serializer(book_list, many=True)
        return Response(book_ser.data)

    def post(self, request):
        book_ser = self.get_serializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})


class PublishGenericDetailView(GenericAPIView):
    # queryset传如queryset对象
    # queryset = Book.objects
    queryset = Publish.objects.all()
    # 使用哪个序列化类来序列化这些数据
    serializer_class = PublishSerializer

    def get(self, request, pk):
        book = self.get_object()
        book_ser = self.get_serializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        book = self.get_object()

        book_ser = self.get_serializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)

        else:
            return Response({'status': status.HTTP_101_SWITCHING_PROTOCOLS, 'msg': '校验失败'})

    def delete(self, request, pk):
        res = self.get_object().delete()
        return Response({'status': status.HTTP_200_OK, 'msg': '删除成功', 'data': res})


# 基于 GenericAPIView的九个方法
class Book3View(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Book3DetailView(GenericAPIView, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Book.objects.all()

    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class Book4View(ListAPIView, CreateAPIView):
class Book4View(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class Book4DetailView(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
class Book4DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 使用ModelViewSet写的5个接口
class Book5View(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        pass


# class Book6View(ViewSetMixin, APIView):  # 一定要放在APiView前面，继承的查找顺序，是按顺序查找的
class Book6View(ViewSetMixin, GenericAPIView):  # 一定要放在APiView前面，继承的查找顺序，是按顺序查找的
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_all_book(self, request):
        print(self.request.data)
        print(request.data)
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)


class Book7View(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # action是装饰器，第一个参数传一个列表，里面放请求方式，第二个参数是detail：布尔类型，
    # 向这个地址发送get请求，会执行下面的函数
    @action(methods=['get', 'post'], detail=False)
    def get_2(self, request):
        book = self.get_queryset()[:2]  # 从0开始截取一条
        ser = self.get_serializer(book, many=True)
        return Response(ser.data)
