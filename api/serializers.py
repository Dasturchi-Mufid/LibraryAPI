from rest_framework import serializers
from book import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn')