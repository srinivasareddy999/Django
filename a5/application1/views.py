from django.shortcuts import render
from application1.models import employees
def srinu(request):
    data=employees.objects.all()
    return render(request,"application1/s1.html",{'data':data})
