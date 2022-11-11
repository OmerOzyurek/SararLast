from django.urls import path
from . import views


urlpatterns = [
    
    path('Colors/',views.ColorsPage,name='ColorsPage'),
    path('Galery/',views.Galery,name='GaleryPage'),
    path('About/',views.About,name='AboutPage'),
    path('Conctact/',views.Contact,name='ContactPage'),
    
]