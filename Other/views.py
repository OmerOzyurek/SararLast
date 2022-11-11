from django.shortcuts import render

# Create your views here.



def ColorsPage(request):
    return render(request,'Other/ColorsPage.html')



def Galery(request):
    return render(request,'Other/GaleryPage.html')



def About(request):
    return render(request,'Other/AboutPage.html')



def Contact(request):
    return render(request,'Other/ContactPage.html')
