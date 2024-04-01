from rest_framework.generics import ListAPIView
from book import models
from . import serializers

class BookAPIView(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
