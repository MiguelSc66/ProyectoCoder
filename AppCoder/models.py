from django.db import models

# Create your models here.
class Family3(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNac = models.DateField()