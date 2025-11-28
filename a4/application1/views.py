from django.shortcuts import render
from application1.models import student
def srinu(request):
    data=student.objects.all()
    return render(request,"application1/s1.html", {'data':data})
