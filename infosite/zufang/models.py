from django.db import models


# Create your models here.
class Zufang_Info(models.Model):
    title = models.CharField(max_length=200)
    month_money = models.CharField(max_length=100)
    mianji = models.CharField(max_length=200)
    img = models.CharField(max_length=300,default="")
