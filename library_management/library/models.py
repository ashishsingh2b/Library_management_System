from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveBigIntegerField()
    category =models.CharField(max_length=50)

class Stundet(models.Model):
    name= models.OneToOneField(User,on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    #image = models.ImageField(upload_to="", blank=True)

