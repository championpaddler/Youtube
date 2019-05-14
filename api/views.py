from django.shortcuts import render

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# Create your views here.
from rest_framework import generics
from .serializers import VideolistSerializer
from .models import Videos


DEVELOPER_KEY = 'AIzaSyCFiJlllzRSpJdwyJ9tnjgW0OaVoCnjRHU'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Videos.objects.all()
    serializer_class = VideolistSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Videos.objects.all().order_by('-publishdatetime')
        query = self.request.query_params.get('query', None)
        queryset = queryset.filter(title__contains=query)
        if(len(queryset)==0):
            search_response = youtube.search().list(q=query,part='id,snippet',maxResults=30).execute()
            for search_result in search_response.get('items', []):
                if search_result['id']['kind'] == 'youtube#video':
                    new = Videos(title=search_result['snippet']['title'],videoid=search_result['id']['videoId'],description=search_result['id']['videoId'],thumbnail=search_result['snippet']['thumbnails']['default']['url'],publishdatetime=search_result['snippet']['publishedAt'])
                    new.save()
            return Videos.objects.all().order_by('-publishdatetime').filter(title__contains=query)
        return queryset

    
    

