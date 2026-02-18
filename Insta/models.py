from django.db import models

# Create your models here.
class Reg(models.Model):
    name=models.CharField(max_length=30)
    reg=models.IntegerField()
    college=models.CharField(max_length=50)
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    sub3=models.IntegerField()
    sub4=models.IntegerField()
    
