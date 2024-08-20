from django.db import models

class Destination(models.Model):
    name= models.URLField(max_length =1000)
    img=models.ImageField(upload_to='pics', null=True, blank=False)
    