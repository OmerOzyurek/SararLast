from django.shortcuts import render
from . models import PVCKAPI

# Create your views here.



def Product(request):
    return render(request,'Product/Product.html')


def ProductDetail(request):
    sorguseti =  PVCKAPI.objects.all()
   
    

    
    context = {
        
        'test':sorguseti
    }
    
   
    return render(request,'Product/ProductDetail.html',context)