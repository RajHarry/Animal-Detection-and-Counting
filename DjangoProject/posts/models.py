from django.db import models

class Image(models.Model): 
    #name = models.CharField(max_length=50) 
    upload_image = models.ImageField(upload_to='images/') 