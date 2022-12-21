from django.db import models
from django.contrib.auth.models import User  


# Create your models here.
class Direccion(models.Model):
    ciudad = models.CharField(max_length=45,null=False,default='')
    calle = models.CharField(max_length=45,null=False)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return self.ciudad + ", " + self.calle 

class Institucion(models.Model):
    nombre = models.CharField(max_length=45,null=False,default='')
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.nombre

class User(models.Model):
    username = models.CharField(max_length=45,null=False,default='')
    password = models.CharField(max_length=45,null=False,default='')
    nombre = models.CharField(max_length=45,null=False,default='')
    apellidoPaterno = models.CharField(max_length=45,null=False,default='')
    apellidoMaterno = models.CharField(max_length=45,null=True,default='')
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    nacimiento = models.DateTimeField(null=True)
    estado = models.BooleanField(null=False,default=True)
    institucion = models.ForeignKey(Institucion,on_delete=models.CASCADE,null=False,default='')

    def __str__(self):
        nombre = self.nombre +" "+ self.apellidoPaterno +" "+ self.apellidoMaterno
        return nombre

class Profesor(models.Model):
    id = models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE,null=False,default='')
    titulo = models.CharField(max_length=45,null=True,default='')
    puntuacion = models.IntegerField(null=True,default='')

class Curso(models.Model):
    nombre = models.CharField(max_length=45,null=False,default='')

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    
    id = models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE,null=False,default='')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    promedio = models.FloatField(null=False,default=7.0)

    def __str__(self):
        nombre = self.id.nombre +" "+ self.id.apellidoPaterno +" "+ self.id.apellidoMaterno
        return nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=45,null=False)
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    fecha = models.DateField(null=False,default='')
    nota = models.FloatField(null=False,default='')

    
    
