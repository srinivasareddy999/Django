from django.shortcuts import render
from application1.models import products
def srinu(request):
    data=products.objects.all()
    return render(request,'application1/s1.html',{'data':data})
