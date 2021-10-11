from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class PersonalizadoBaseUserManager(BaseUserManager):
    def create_user(self,usuario, password):
        if not usuario:
            raise ValueError("Tiene que tener un usuario")
        if not password:
            raise ValueError("Tiene que tener contraseña")
        user_obj = self.model(usuario = usuario)
        user_obj.set_password(password)
        user_obj.is_admin = False
        user_obj.is_active = True
        user_obj.save(using=self.db)
        return user_obj

    def create_superuser(self, usuario, password):
        user = self.create_user(usuario, password)
        user.is_admin = True
        return user

class Usuario (AbstractBaseUser):
    nombre_completo = models.CharField(unique=True, max_length=200)
    usuario = models.CharField(unique=True,max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'usuario'

    REQUIRED_FIELDS = []

    objects = PersonalizadoBaseUserManager()

    def get_full_name(self):
        return self.usuario

    def get_short_name(self):
        return self.usuario

    def __str__(self):
        return self.nombre_completo
    
    @property
    def is_admin(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.is_active