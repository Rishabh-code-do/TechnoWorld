from django.db import models

# Create your models here.

class content(models.Model):
    img1=models.ImageField(upload_to='pics')
    name= models.CharField(max_length=500)
    price= models.IntegerField()
    des= models.CharField(max_length=5000)

class category(models.Model):
    cat=models.CharField(max_length=500)