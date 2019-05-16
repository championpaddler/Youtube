from django.db import models

# Create your models here.
class Videos(models.Model):
    """This class represents the Videos model."""
    title = models.TextField(null=False,db_index=True)
    videoid = models.CharField(null=False,max_length=100)
    description = models.TextField(null=False)
    thumbnail = models.TextField(null=False)
    publishdatetime = models.DateTimeField(null=False)