from pyexpat import model
from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()
    fecha= models.DateField()