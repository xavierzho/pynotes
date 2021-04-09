from rest_framework import serializers
from api import models


# 重写ListSerializer,重写update方法
class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        """

        :param instance: 对象列表[book1, book2],
        :param validated_data: 需要修改的数据列表[{name:xxx,price:xxx},{name:xxx,price:xxx},]
        :return:
        """
        ...
        print(instance)
        print(validated_data)
        # 保存数据
        return [
            self.child.update(instance[i], attrs) for i, attrs in enumerate(validated_data)
        ]


# 如果序列化的是数据库的表，尽量用ModelSerializer
class BookModelSerializer(serializers.ModelSerializer):
    # 方案一：只序列化可以，反序列化有问题
    # publish = serializers.CharField(source='publish.name')
    # 方案二：models中可以写方法

    class Meta:
        # 修改多条数据的方式二：
        # list_serializer_class = BookListSerializer
        model = models.Book
        fields = ('id', 'name', 'price', 'authors', 'publish', 'publish_name', 'author_list')
        depth = 0
        extra_kwargs = {
            'publish': {'write_only': True},
            'publish_name': {'read_only': True},
            'authors': {'write_only': True},
            'author_list': {'read_only': True},
        }
