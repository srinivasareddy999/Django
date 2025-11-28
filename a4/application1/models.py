from django.db import models
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=21)
    sec=models.CharField(max_length=12)
    J_date=models.DateField()
    gender=models.CharField(max_length=12)
