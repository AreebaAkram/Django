from django.db import models

# Create your models here.
class date(models.Model):
    Date= models.DateField(primary_key=True)

class task(models.Model):
    Date= models.ForeignKey(date, on_delete=models.CASCADE)
    Name= models.CharField(max_length=10)
    Description= models.CharField(max_length=200)
    Note= models.CharField(max_length=50)
    Date_created=models.DateField(auto_now_add=True)
    Time=models.TimeField(auto_now_add=True)
