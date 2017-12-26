from datetime import datetime
from django.db import models

# Create your models here.


class Location(models.Model):
  username = models.TextField(max_length=20, unique=True)
  latitude = models.FloatField()
  longitude = models.FloatField()
  update_time = models.DateTimeField(auto_now=True)
  spacing = models.IntegerField(null=True, blank=True)
