from django import forms
from app import models

formatoFecha = [
    '%d/%m/%Y %H:%M:%S',    
    '%d/%m/%Y %H:%M',      
    '%d/%m/%Y',            
    '%d/%m/%y %H:%M:%S',   
    '%d/%m/%y %H:%M',      
    '%d/%m/%y',   
    '%d-%m-%Y %H:%M:%S',   
    '%d-%m-%Y %H:%M',      
    '%d-%m-%Y',            
    '%d-%m-%y %H:%M:%S',   
    '%d-%m-%y %H:%M',      
    '%d-%m-%y'             
    ]

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = models.Profesor
        fields = '__all__'

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=45,required=True)

class AsignaturaForm(forms.Form):
    nombre = forms.CharField(max_length=45,required=True)

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=45,label='Nombre',required=True)
    apellidoPaterno = forms.CharField(max_length=45,label='Apellido paterno',required=True)
    apellidoMaterno = forms.CharField(max_length=45,label='Apellido materno',required=False)
    nacimiento = forms.DateTimeField(label='Fecha Nacimiento',required=True,input_formats=formatoFecha)

    ciudad = forms.CharField(max_length=45,label='Ciudad',required=True)
    calle = forms.CharField(max_length=45,label='Calle',required=True)
    numero = forms.CharField(max_length=45,label='Numero',required=False)

    institucion = forms.ModelChoiceField(queryset=models.Institucion.objects.all(),widget=forms.Select(attrs={
        'class':'form-control'
    }))
    curso = forms.ModelChoiceField(queryset=models.Curso.objects.all(),widget=forms.Select(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(max_length=45,label='Contraseña',required=True)

class CalificacionForm(forms.Form):

    curso = forms.ModelChoiceField(queryset=models.Curso.objects.all(),required=True,widget=forms.Select(attrs={
        'class':'form-control'
    }))
    alumnos = forms.ModelChoiceField(queryset=models.Alumno.objects.none(),required=True,widget=forms.Select(attrs={
        'class':'form-control'
    }))
    asignatura = forms.ModelChoiceField(queryset=models.Asignatura.objects.all(),required=True,widget=forms.Select(attrs={
        'class':'form-control'
    }))
    profesor = forms.ModelChoiceField(queryset=models.Profesor.objects.all(),required=False,widget=forms.Select(attrs={
        'class':'form-control'
    }))
    nota = forms.FloatField(max_value=7.0,min_value=1.0,required=True)
    
class InstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=45,required=True)

class DireccionForm(forms.Form):
    ciudad = forms.CharField(max_length=45,required=True)
    calle = forms.CharField(max_length=45,required=True)
    numero = forms.IntegerField(required=False)

