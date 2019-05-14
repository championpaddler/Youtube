from django.db import models

# Create your models here.
class Videos(models.Model):
    """This class represents the bucketlist model."""
    title = models.TextField(null=False)
    videoid = models.TextField(null=False)
    description = models.TextField(null=False)
    thumbnail = models.TextField(null=False)
    publishdatetime = models.DateTimeField(null=False)