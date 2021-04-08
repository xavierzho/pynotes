from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from . import models, serializer


class BookView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer
