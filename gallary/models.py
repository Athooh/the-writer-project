from django.db import models

# Create your models here.
class Gallary(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    
class Gallary2(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')