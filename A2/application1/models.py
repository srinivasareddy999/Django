from django.db import models
class employees(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=12)
    company=models.CharField(max_length=12)
    designation=models.CharField(max_length=12) 
    J_date=models.DateField()  
