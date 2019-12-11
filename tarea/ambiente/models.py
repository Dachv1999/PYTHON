from django.db import models
from django.urls import reverse

class Ambiente (models.Model):
    nombre_ambiente = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('ambiente:ambiente-list')

    def __str__(self):
        return self.nombre_ambiente


