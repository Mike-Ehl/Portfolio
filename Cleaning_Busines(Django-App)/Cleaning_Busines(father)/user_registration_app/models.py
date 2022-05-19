from re import M
from django.db import models



class Picture(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100) 
    onemorefield = models.DateField()