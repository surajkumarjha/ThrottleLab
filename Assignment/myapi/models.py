from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.functions import Now
import uuid
import datetime


class User(models.Model):


    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.real_name

# Create your models here.
