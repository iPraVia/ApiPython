from rest_framework import serializers
from datetime import datetime  
from app.models import *

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):

    direccion = DireccionSerializer()

    class Meta:
        model = Institucion
        fields = '__all__'

    def create(self,validated_data):
        direccion_data = validated_data.pop('direccion')
        direcion = Direccion.objects.create(**direccion_data)
        institucion = Institucion.objects.create(direccion=direcion,**validated_data)
        return institucion
    
    def update(self,instance,validated_data):
        institucion_data = validated_data.pop('direccion')
        institucion = instance.direccion

        instance.direccion.ciudad = institucion_data.get('ciudad',instance.direccion.ciudad)
        instance.direccion.calle = institucion_data.get('calle',instance.direccion.calle)
        instance.direccion.numero = institucion_data.get('numero',instance.direccion.numero)
        instance.save()
        institucion.save()

        return instance
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    direccion = DireccionSerializer()

class ProfesorSerializer(serializers.ModelSerializer):

    id = UserSerializer()

    class Meta:
        model = Profesor
        fields = '__all__'
    
    def create(self, validated_data):
        user = validated_data.pop('id')
        datos = user.pop('direccion')
        direccion = Direccion.objects.create(**datos)
        user = User.objects.create(direccion=direccion,**user)
        profesor = Profesor.objects.create(id=user,**validated_data)
        return profesor
       

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):

    id = UserSerializer()
    

    class Meta:
        model = Alumno
        fields = '__all__'
    
    def create(self, validated_data):
        user = validated_data.pop('id')
        datos = user.pop('direccion')
        direccion = Direccion.objects.create(**datos)
        user = User.objects.create(direccion=direccion,**user)
        alumno = Alumno.objects.create(id=user,**validated_data)
        return alumno

class AsignaturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asignatura
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calificacion
        fields = '__all__'    

    def create(self, validated_data):
        validated_data['fecha'] = datetime.strftime(validated_data['fecha'],'%Y-%m-%d')
        validarNota = lambda n: True if (int(n) >= 0 and int(n) <=7) else False
        calificacion = Calificacion.objects.create(**validated_data)
        if(validarNota(validated_data['nota'])):
            return calificacion












