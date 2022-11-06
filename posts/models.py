from django.db import models
from django.forms import CharField, DateTimeField
from datetime import date, datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(default = "" , max_length=20)
    body= models.CharField(default = "" ,max_length=500)
    createdAt=models.DateTimeField( default=datetime.now, blank=True)

