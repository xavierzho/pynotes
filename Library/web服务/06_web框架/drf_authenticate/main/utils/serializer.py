from rest_framework import serializers
from main.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Book2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'publish')


