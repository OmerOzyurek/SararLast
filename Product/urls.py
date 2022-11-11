from django.urls import path
from . import views


urlpatterns = [
    
    path('Pr/',views.Product,name='ProductPage'),
    path('PrDt/',views.ProductDetail,name='ProductDetail')
    
]