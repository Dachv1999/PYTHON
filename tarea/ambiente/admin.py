from django.contrib import admin
from .models import Ambiente

class AmbienteAdminPage(admin.ModelAdmin):
    list_display = ('nombre_ambiente', 'id')

admin.site.register(Ambiente, AmbienteAdminPage)
