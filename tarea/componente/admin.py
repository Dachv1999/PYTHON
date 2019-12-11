from django.contrib import admin
from .models import Componente

class ComponenteAdminPage (admin.ModelAdmin):
    list_display = ('nombre_componente', 'id', 'identificador', 'descripcion')

admin.site.register(Componente, ComponenteAdminPage)
