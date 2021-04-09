from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSetMixin
from rest_framework.decorators import action
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Book, Publish
from serializers.bookSer import BookSerializer, BookModelSerializer
from serializers.publishSer import PublishModelSerializer
from response.customResponse import Message


# 基于APIView
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


class BooksViewByModelSer(APIView):
    def get(self, request):
        response_msg = {'status': 200, 'msg': 'OK'}
        books = Book.objects.all()
        book = Book.objects.all().first()
        books_ser = BookModelSerializer(books, many=True)
        book_ser = BookModelSerializer(book)
        print(type(book_ser), type(books_ser))
        response_msg['data'] = book_ser.data
        return Response(response_msg)


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


# 基于GenericAPIView,传入queryset和serializer_class，自动识别方法
class BookGenericView(GenericAPIView):
    queryset = Book.objects.all()
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
    queryset = Publish.objects.all()
    # 使用哪个序列化类来序列化这些数据
    serializer_class = PublishModelSerializer

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
    queryset = Publish.objects.all()

    serializer_class = PublishModelSerializer

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
class BookGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookGenericAPIDetailView(GenericAPIView, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Book.objects.all()

    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class Book4View(ListAPIView, CreateAPIView):  # ListAPIView(getS), CreateAPIView(POST)集成ListCreateAPIView
# 继承mixin基类+GenericAPIView
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class Book4DetailView(RetrieveAPIView, DestroyAPIView, UpdateAPIView):  # RetrieveAPIView(GET), DestroyAPIView(DELETE), UpdateAPIView(PUT)集成RetrieveUpdateDestroyAPIView
# 继承mixin基类+GenericAPIView
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 使用ModelViewSet写的5个接口
class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        pass


# class Book6View(ViewSetMixin, APIView):  # 一定要放在APiView前面，继承的查找顺序，是按顺序查找的
class BookGenericViewSet(ViewSetMixin, GenericAPIView):  # 一定要放在APiView前面，继承的查找顺序，是按顺序查找的
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_all_book(self, request):
        # 取别名的写法
        print(self.request.data)
        print(request.data)
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)


class BooksModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # action是装饰器，第一个参数传一个列表，里面放请求方式，第二个参数是detail：布尔类型，
    # 向这个地址发送get请求，会执行下面的函数
    @action(methods=['get', 'post'], detail=False)
    def get_2(self, request):
        book = self.get_queryset()[:2]  # 从0开始截取一条
        ser = self.get_serializer(book, many=True)
        return Response(ser.data)
