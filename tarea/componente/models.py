from django.db import models
from django.urls import reverse
from ambiente.models import Ambiente

class Componente (models.Model):
    ambiente = models.ForeignKey(Ambiente, null=True, blank= True, on_delete=models.CASCADE)
    nombre_componente = models.CharField(max_length=200)
    identificador = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('componente:componente-list')

    def __str__(self):
        return self.nombre_componente

