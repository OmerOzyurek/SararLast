from django.db import models


class PVCKAPI(models.Model):
    Baslik = models.CharField(max_length=100)
    no = models.IntegerField(auto_created=True)
    KapiModeli = models.CharField(max_length=20)
    Aciklama = models.CharField(max_length=150)
    Resim_261 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))
    Resim_283 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))
    Resim_284 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))
    Resim_288 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))
    Resim_292 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))
    Resim_294 = models.ImageField(null=True,blank=True,upload_to=('Baslik'))

    
    
    
    