from django.db import models
class products(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=21)
    price=models.FloatField()
    company=models.CharField(max_length=21)
    M_date=models.DateField()
    E_date=models.DateField()