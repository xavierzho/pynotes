"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from rest_framework import serializers
from ..models import Publish


class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'
