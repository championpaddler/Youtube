from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Videos

class VideolistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Videos
        fields = ('title','description','thumbnail','publishdatetime','videoid')

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
