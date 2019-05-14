from django.shortcuts import render

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# Create your views here.
from rest_framework import generics
from .serializers import VideolistSerializer
from .models import Videos


DEVELOPER_KEY = 'REPLACE_ME'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Videos.objects.all()
    serializer_class = VideolistSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Videos.objects.all()
        query = self.request.query_params.get('query', None)
        queryset = queryset.filter(title=query)
        if(len(queryset)==0):
            print("Ok")
        return queryset