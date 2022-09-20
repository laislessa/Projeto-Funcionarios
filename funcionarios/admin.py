from django.contrib import admin

from .models import Departamento, Perfil, Funcionarios

admin.site.register(Perfil)
admin.site.register(Funcionarios)
admin.site.register(Departamento)

# Register your models here.