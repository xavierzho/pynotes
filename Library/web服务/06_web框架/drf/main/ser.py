from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from main.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, source='nid')
    name = serializers.CharField(min_length=2, max_length=16)
    price = serializers.CharField(write_only=True)
    author = serializers.CharField()
    publish = serializers.CharField()
    authors = serializers.SerializerMethodField()

    def get_authors(self, instance):
        # book对象
        authors = instance.authors.all()
        lis = []
        for author in authors:
            lis.append(author.name)
        return lis

    def update(self, instance, validated_data):
        """

        :param instance: book对象
        :param validated_data: 校验后的数据
        :return:
        """
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.publish = validated_data.get('publish')
        instance.save()
        return instance

    def create(self, validated_data):
        instance = Book.objects.create(**validated_data)
        return instance

    def validate_price(self, data):
        if float(data) > 10:
            return data
        else:
            # 校验失败，抛异常
            raise ValidationError('价格不能低于10元')

    def validate(self, attrs):
        author = attrs.get('author')
        publish = attrs.get('publish')
        print(author, publish)
        if author == publish:
            raise ValidationError('作者名和出版社不能相同')
        else:
            return attrs


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # 对应上models.py中的模型
        # fields = '__all__'  # 将所有的字段序列化
        # fields = ('name', 'price', 'publish')  # 部分字段序列化
        exclude = ('name',)  # 排除name字段， 不能根fields同时存在
        # read_only_fields = ('nid',)
        # write_only_fields = ('price',)
        extra_kwargs = {
            'nid': {'read_only': True, 'required': True},
            'price': {'write_only': True, 'required': True},
        }
