from django.db import models

# Create your models here.

class Formulario(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Cedula = models.PositiveIntegerField(unique=True)
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    Edad = models.PositiveIntegerField()
    Casado = models.BooleanField(default=False)

    def NombreCompleto(self):
        cadena = "{0}  {1}, {2}"
        return cadena.format(self.Nombre, self.Apellido, self.Sexo)

    def __str__(self):
        return self.NombreCompleto()

    def FindAll():
        return Formulario.objects.all()
    
    def Find(cedula):
        return Formulario.objects.filter(Cedula=cedula)

    def Create(data):
        form=Formulario()
        form.Nombre=data.Nombre
        form.Apellido=data.Apellido
        form.Cedula=data.Cedula
        form.Sexo=data.Sexo
        form.Edad=data.Edad
        form.Casado=data.Casado
        form.save()

    def Update(cedula,form):
        Formulario.Find(cedula).update(Nombre=form.Nombre,Apellido=form.Apellido,Sexo=form.Sexo,Edad=form.Edad,Casado=form.Casado)

    def delete(cedula):
        Formulario.Find(cedula).delete()
