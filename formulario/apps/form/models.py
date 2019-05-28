from django.db import models

# Create your models here.


class Dao(models.Model):
    def Remove(self,cedula):
        self.Find(cedula).delete()

    def FindAll(self):
        return self.objects.all()

    def is_empty(self):
        return self.objects.count()==0

    def Create(self):
        self.save()

    class Meta:
        abstract = True


class Formulario(Dao):
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))

    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Cedula = models.PositiveIntegerField(unique=True)
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    Edad = models.PositiveIntegerField()
    Casado = models.BooleanField(default=False)

    def __str__(self):
        cadena = "{0} {1},{2}"
        return cadena.format(self.Nombre, self.Apellido, self.Cedula)
    
    def Find(cedula):
        return Formulario.objects.filter(Cedula=cedula)
    
    def Update(cedula,data):
        Formulario.Find(cedula).update(Nombre=data.Nombre,Apellido=data.Apellido,Sexo=data.Sexo,Edad=data.Edad,Casado=data.Casado)
