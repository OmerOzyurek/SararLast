from django.shortcuts import render

# Create your views here.



def Product(request):
    return render(request,'Product/Product.html')


def ProductDetail(request):
    return render(request,'Product/ProductDetail.html')