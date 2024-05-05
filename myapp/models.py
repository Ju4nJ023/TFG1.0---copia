from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre de la parada')
    address= models.CharField(max_length=250, verbose_name='Dirección de la parada')
    latitude = models.FloatField(verbose_name='Latitud')
    longitude = models.FloatField(verbose_name='Longitud')
   
    
    
    class Meta:
        verbose_name = 'parada'
        verbose_name_plural = 'paradas'
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Asiento(models.Model):
    numero = models.IntegerField()
    disponible = models.BooleanField(default=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    
