from rest_framework import serializers
from .models import Videos

class VideolistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Videos
        fields = ('title','description','thumbnail','publishdatetime')
