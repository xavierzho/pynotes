from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from utils.response import APIResponse
from utils.serializer import BookModelSerializer
from utils.throttle import IPThrottle
from . import models


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs.get('pk'))
        # 查单个和查询所有，合并到一起
        if kwargs.get('pk'):
            # print(111)
            # 查单个
            book = models.Book.objects.filter(pk=kwargs.get('pk')).first()

            book_ser = BookModelSerializer(book)

            return APIResponse(data=book_ser.data)
        else:
            # 查所有
            book_list = models.Book.objects.all().filter(is_delete=False)

            book_ser = BookModelSerializer(book_list, many=True)
            return APIResponse(data=book_ser.data)

    def post(self, request, *args, **kwargs):
        """
        这个接口具备增多条和增一条的功能
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if isinstance(request.data, dict):

            book_ser = BookModelSerializer(data=request.data)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return APIResponse(data=book_ser.data)
        elif isinstance(request.data, list):
            # 这是个ListSerializer
            list_model_book_ser = BookModelSerializer(data=request.data, many=True)
            # print(type(list_model_book_ser))
            list_model_book_ser.is_valid(raise_exception=True)
            """
            新增-->rest_framework.serializers.ListSerializer-->create方法
                def create(self, validated_data):
                    # self.child是BookModelSerializer的对象
                    print(type(self.child))
                    return [
                        self.child.create(attrs) for attrs in validated_data
                    ]
            """
            list_model_book_ser.save()
            return APIResponse(data=list_model_book_ser.data)

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk:
            # 改一条
            book = models.Book.objects.filter(pk=pk).first()
            # partial=True可以局部修改，不必把所有数据带上
            book_ser = BookModelSerializer(instance=book, data=request.data, partial=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return APIResponse(data=book_ser.data)
        else:
            # 改多条
            # 前端传来的数据格式：[{id:1,name:xxx,price:xxx},{id:1,name:xxx,price:xxx},]
            # 处理传来的数据，对象列表[book1, book2],需要修改的数据列表[{name:xxx,price:xxx},{name:xxx,price:xxx},]
            book_list = []
            modify_data = []
            if isinstance(request.data, list):
                for item in request.data:
                    print(item)
                    pk = item.pop('id')
                    book = models.Book.objects.get(pk=pk)
                    book_list.append(book)
                    modify_data.append(item)
                # 方案一：for循环一个一个修改,不需要重写

                for i, book in enumerate(modify_data):
                    book_ser = BookModelSerializer(instance=book_list[i], data=book)
                    book_ser.is_valid(raise_exception=True)
                    book_ser.save()
                return APIResponse(data='modify multi OK')
            # 方案二：重写ListSerializer
            #     book_ser = BookModelSerializer(data=modify_data, many=True, instance=book_list)
            #     book_ser.is_valid(raise_exception=True)
            #     book_ser.save()
            #     return APIResponse(data=book_ser.data)

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        pks = []
        if pk:
            # 单个删除
            pks.append(pk)
            # 不管是单个删除还是批量删除只使用批量方法删除
        else:
            # 批量删除
            pks = request.data.get('pks')
        res = models.Book.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        # 删除的条数

        if res:
            return APIResponse(msg=f'删除{res}条数据')
        else:
            return APIResponse(msg='没有要删除的数据')


class BookGenericAPIView(GenericAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            # print(111)
            # 查单个
            book = self.get_object()

            book_ser = self.get_serializer(book)

            return APIResponse(data=book_ser.data)
        else:
            # 查所有
            book_list = self.get_queryset()

            book_ser = self.get_serializer(book_list, many=True)
            return APIResponse(data=book_ser.data)

    def post(self, request, *args, **kwargs):
        """
        这个接口具备增多条和增一条的功能
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if isinstance(request.data, dict):

            book_ser = self.get_serializer(data=request.data)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return APIResponse(data=book_ser.data)
        elif isinstance(request.data, list):
            # 这是个ListSerializer
            list_model_book_ser = self.get_serializer(data=request.data, many=True)
            # print(type(list_model_book_ser))
            list_model_book_ser.is_valid(raise_exception=True)
            """
            新增-->rest_framework.serializers.ListSerializer-->create方法
                def create(self, validated_data):
                    # self.child是BookModelSerializer的对象
                    print(type(self.child))
                    return [
                        self.child.create(attrs) for attrs in validated_data
                    ]
            """
            list_model_book_ser.save()
            return APIResponse(data=list_model_book_ser.data)

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk:
            # 改一条
            book = self.get_object()
            # partial=True可以局部修改，不必把所有数据带上
            book_ser = self.get_serializer(instance=book, data=request.data, partial=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return APIResponse(data=book_ser.data)
        else:
            # 改多条
            # 前端传来的数据格式：[{id:1,name:xxx,price:xxx},{id:1,name:xxx,price:xxx},]
            # 处理传来的数据，对象列表[book1, book2],需要修改的数据列表[{name:xxx,price:xxx},{name:xxx,price:xxx},]
            book_list = []
            modify_data = []
            if isinstance(request.data, list):
                for item in request.data:
                    print(item)
                    pk = item.pop('id')
                    book = models.Book.objects.get(pk=pk)
                    book_list.append(book)
                    modify_data.append(item)
                # 方案一：for循环一个一个修改,不需要重写

                for i, book in enumerate(modify_data):
                    book_ser = self.get_serializer(instance=book_list[i], data=book)
                    book_ser.is_valid(raise_exception=True)
                    book_ser.save()
                return APIResponse(data='modify multi OK')
            # 方案二：重写ListSerializer
            #     book_ser = BookModelSerializer(data=modify_data, many=True, instance=book_list)
            #     book_ser.is_valid(raise_exception=True)
            #     book_ser.save()
            #     return APIResponse(data=book_ser.data)

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        pks = []
        if pk:
            # 单个删除
            pks.append(pk)
            # 不管是单个删除还是批量删除只使用批量方法删除
        else:
            # 批量删除
            pks = request.data.get('pks')

        res = self.get_queryset().filter(pk__in=pks, is_delete=False).update(is_delete=True)
        # 删除的条数

        if res:
            return APIResponse(msg=f'删除{res}条数据')
        else:
            return APIResponse(msg='没有要删除的数据')


class PagerNumber(PageNumberPagination):
    # 每页显示多少条数据
    page_size = 3
    # url中翻页的参数名
    page_query_param = 'page'
    # url路径上的参数名
    page_size_query_param = 'size'
    # 最大每页展示多少条数据
    max_page_size = 10


class PagerLimit(LimitOffsetPagination):
    # 每页显示多少条数据
    default_limit = 3
    # url参数名：每页显示多少条
    limit_query_param = 'limit'
    # url参数名：第几条数据开始
    offset_query_param = 'offset'
    # 最大显示多少条
    max_limit = 10


class PagerCursor(CursorPagination):
    # 每页查询的key
    cursor_query_param = 'cursor'
    # 一页显示多少条数据
    page_size = 2
    # 最大显示多少条数据
    max_page_size = 10
    # 排序字段
    ordering = '-create_time'


class BookView(ListAPIView):
    """
    返回所有的图书信息
    """
    queryset = models.Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = PagerNumber


class BookView2(APIView):
    throttle_classes = [IPThrottle]

    def get(self, request, *args, **kwargs):
        """
        这个一会能看到效果
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        books = models.Book.objects.all().order_by('create_time')

        pager = PagerNumber()
        books = pager.paginate_queryset(books, request, view=self)
        # 方案一：直接调用内置get_paginated_response方法返回
        ser = BookModelSerializer(instance=books, many=True)
        # return pager.get_paginated_response(ser.data)
        # 方案二：
        next_url = pager.get_next_link()
        previous_url = pager.get_previous_link()
        return APIResponse(data=ser.data, next_url=next_url, previous_url=previous_url)

    def post(self, request, *args, **kwargs):
        """
        新建书信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return
