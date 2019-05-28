from django.contrib import admin
from .models import Formulario

# Register your models here.

class FormularioAdmin(admin.ModelAdmin):
    fieldsets=[
        ('DatosPersonal',{'fields':['Nombre','Apellido','Cedula','Sexo','Edad','Casado']})
    ]
    list_display=('Nombre','Apellido','Cedula','Sexo','Edad','Casado')
    list_filter=['Casado']
    search_fields=['Nombre','Apellido']

admin.site.register(Formulario,FormularioAdmin)