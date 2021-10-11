from django.contrib import admin
from .models import Usuario

class UsuarioAdminPage(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'usuario') 

admin.site.register(Usuario, UsuarioAdminPage)
