from django.db import models

# Crlass place (modeeate your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

def __str__(self):
     return self.name
