from django.db import models

# Create your models here.
class Videos(models.Model):
    """This class represents the bucketlist model."""
    title = models.TextField()
    description = models.TextField()
    thumbnail = models.TextField()
    publishdatetime = models.DateTimeField(auto_now_add=True)