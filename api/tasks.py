from celery.task.schedules import crontab
from celery.decorators import periodic_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.db.models.fields import DateField
from django.db.models.functions import Cast

from datetime import datetime
from api.models import Videos
DEVELOPER_KEY = 'AIzaSyCnzBS9oaJuc9TqRPSNsKK_Fwf8vlX2haA'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

# Perodic Task to fetch latest and trending videos and save in db.
@periodic_task(run_every=(crontab(minute='*/7200')), name="some_task", ignore_result=True)
def some_task():
    #Fetch Latest Video Date
    date = list(Videos.objects.order_by('-publishdatetime')[:1].values('publishdatetime'))[0]['publishdatetime']
    date=date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    try :
        search_response = youtube.search().list(part='id,snippet',regionCode='IN',order='viewCount',maxResults=50,type='video',publishedAfter=date).execute()
        for search_result in search_response.get('items', []):
            Videos(title=search_result['snippet']['title'],videoid=search_result['id']['videoId'],description=search_result['snippet']['description'],thumbnail=search_result['snippet']['thumbnails']['default']['url'],publishdatetime=search_result['snippet']['publishedAt']).save()
    except :
        print("Error Occured")
    