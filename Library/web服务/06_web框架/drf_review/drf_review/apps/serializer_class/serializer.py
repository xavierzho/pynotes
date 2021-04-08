from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    publish_name = serializers.CharField(read_only=True, source='publish.name')

    class Meta:
        model = models.Book
        fields = ('name', 'publish_name', 'publish_date', 'author_list', 'language_name', 'publish', 'authors', 'price')
        extra_kwargs = {
            'publish': {'write_only': True},
            # 'publish_name': {'read_only': True, 'source': 'publish.name'},
            'authors': {'write_only': True},
            'author_list': {'read_only': True}
        }

