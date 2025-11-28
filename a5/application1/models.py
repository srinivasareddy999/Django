from django.db import models
class employees(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=21)
    company=models.CharField(max_length=21)
    des=models.CharField(max_length=12)
    location=models.CharField(max_length=21)
    salary=models.FloatField()
