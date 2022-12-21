from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app import forms
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, filters
from django.http import Http404
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend 

formatosFecha = ['%d/%m/%Y %H:%M:%S','%d/%m/%Y %H:%M','%d/%m/%Y','%d/%m/%y %H:%M:%S','%d/%m/%y %H:%M','%d/%m/%y','%d-%m-%Y %H:%M:%S','%d-%m-%Y %H:%M','%d-%m-%Y','%d-%m-%y %H:%M:%S','%d-%m-%y %H:%M','%d-%m-%y']

def formatFecha(fecha):
    newFecha = None
    for f in formatosFecha:
        try:
            newFecha = datetime.strptime(fecha,f)
            break
        except:
            continue
    if(newFecha != None):
        return newFecha
    
def index(request):
    return render(request, "index.html")

#CURSO

def panelCurso(request):
    cursos = Curso.objects.all()
    data = {"cursos": cursos}
    return render(request, "curso/panelCurso.html", data)

class CursoView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request) 

    def delete(self, request, pk):
        return self.destroy(request, pk)   

class CursoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 
    


#ASIGNATURA

def panelAsignatura(request):
    asignaturas = Asignatura.objects.all()
    data = {"asignaturas": asignaturas}
    return render(request, "asignatura/panelAsignatura.html", data)

class AsignaturaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)   

class AsignaturaDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk) 

    def delete(self, request, pk):
        return self.destroy(request, pk) 
        

#USUARIO

def panelUser(request):
    users = User.objects.all()
    data = {"users": users}
    return render(request, "user/panelUser.html", data)

class UserView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 

#ALUMNO

def panelAlumno(request):
    alumnos = Alumno.objects.all()
    data = {"alumnos": alumnos}
    return render(request, "user/panelAlumno.html", data)

class AlumnoView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class AlumnoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 

#PROFESOR

def panelProfesor(request):
    profesores = Profesor.objects.all()
    data = {"profesores": profesores}
    return render(request, "user/panelProfesor.html", data)

class ProfesorView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['puntuacion']
    ordering_fields = ['puntuacion']

    filterset_fields = {
    'puntuacion': ['gte']   
}

class ProfesorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 


#INSTITUCION

def panelInstitucion(request):
    instituciones = Institucion.objects.all()
    data = {"instituciones": instituciones}
    return render(request, "institucion/panelInstitucion.html", data)

class InstitucionView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class InstitucionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 

# DIRECCION

def panelDireccion(request):
    direcciones = Direccion.objects.all()
    data = {"direcciones": direcciones}
    return render(request, "direccion/panelDireccion.html", data)

class DireccionView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class DireccionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) 

#CALIFICACION

def panelCalificacion(request):
    calificaciones = Calificacion.objects.all()
    datos = {'calificacion':calificaciones}
    return render(request,'calificacion/panelCalificacion.html',datos)
    
class CalificacionView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nota']
    ordering_fields = ['nota']

    filterset_fields = {
    'nota': ['gte','lte']  }

class CalificacionDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

"""

def panelCurso(request):
    formCurso = forms.CursoForm()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        curso = Curso()
        if( len(nombre) > 0 ):
            curso.nombre = nombre
            respuesta = curso.save()
            curso = Curso.objects.all()
    datos = {'form':formCurso,'cursos':cursos}
    return render(request,'curso/panelCurso.html',datos)

def editarCurso(**id):
    curso = Curso.objects.get(id=id)
    print(curso.nombre)

def borrarCurso(**id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('../panelCurso')

def panelAsignatura(request):
    formAsignatura = forms.AsignaturaForm()
    asignaturas = Asignatura.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        asignatura = Asignatura()
        if( len(nombre) > 0 ):
            asignatura.nombre = nombre
            asignatura.save()
    datos = {'form':formAsignatura,'asignaturas':asignaturas}
    return render(request,'asignatura/panelAsignatura.html',datos)

def editarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    print(asignatura.nombre)

def borrarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    asignatura.delete()
    return redirect('../panelAsignatura')

def panelAlumno(request,id):
    alumno = AlumnoForm()
    datos = {'form':alumno}
    return render(request,'panelAlumno.html',datos)


def panelRegistroAlumno(request):
    formAlumno = AlumnoForm()
    alumnos = Alumno.objects.all()
    if request.method == 'POST':
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            nombre = formAlumno['nombre'].value()
            apellidoPaterno = formAlumno['apellidoPaterno'].value()
            apellidoMaterno = formAlumno['apellidoMaterno'].value()
            fecha = formAlumno['nacimiento'].value()
            nacimiento = formatFecha(fecha)
            ciudad = formAlumno['ciudad'].value()
            calle = formAlumno['calle'].value()
            numero = formAlumno['numero'].value()
            institucionForm = formAlumno['institucion'].value()
            cursoForm = formAlumno['curso'].value()
            password = formAlumno['password'].value()
            curso = Curso.objects.get(id=cursoForm[0])
            institucion = Institucion.objects.get(id=institucionForm[0])
            direccion = Direccion()
            direccion.ciudad = ciudad
            direccion.calle = calle
            if numero.isnumeric():
                direccion.numero = numero
            direccion.save()
            direcciones = Direccion.objects.all()
            direccion = direcciones[len(direcciones)-1]

            usuario = User()
            usuario.username = nombre.strip()[0] + apellidoPaterno.strip() + fecha[3:5]
            usuario.password = password
            usuario.nombre = nombre
            usuario.apellidoPaterno = apellidoPaterno
            usuario.apellidoMaterno = apellidoMaterno
            usuario.direccion = direccion
            usuario.nacimiento = nacimiento
            usuario.institucion = institucion
            usuario.save()

            usuarios = User.objects.all()
            usuario = usuarios[len(usuarios) -1]
            alumno = Alumno()
            alumno.id = usuario
            alumno.curso = curso
            alumno.save()
            print("Usuario almacenado correctamente")

    datos = {'forms':formAlumno,'alumnos':alumnos}
    return render(request,'alumno/panelRegistroAlumno.html',datos)

def panelCurso(request):
    formCurso = forms.CursoForm()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        curso = Curso()
        if( len(nombre) > 0 ):
            curso.nombre = nombre
            respuesta = curso.save()
            curso = Curso.objects.all()
    datos = {'form':formCurso,'cursos':cursos}
    return render(request,'curso/panelCurso.html',datos)

def editarCurso(**id):
    curso = Curso.objects.get(id=id)
    print(curso.nombre)

def borrarCurso(**id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('../panelCurso')

def panelAsignatura(request):
    formAsignatura = forms.AsignaturaForm()
    asignaturas = Asignatura.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        asignatura = Asignatura()
        if( len(nombre) > 0 ):
            asignatura.nombre = nombre
            asignatura.save()
    datos = {'form':formAsignatura,'asignaturas':asignaturas}
    return render(request,'asignatura/panelAsignatura.html',datos)

def editarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    print(asignatura.nombre)

def borrarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    asignatura.delete()
    return redirect('../panelAsignatura')


def panelAdministrador(request):
    return render(request, 'panelAdministrador.html')


class listaProfesor(APIView):
    def get(self, request):
        profesor = Profesor.objects.all()
        serializer = ProfesorSerializer(profesor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfesorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleProfesor(APIView):
    def get_object(self, pk):
        try:
            return Profesor.objects.get(pk=pk)
        except Profesor.DoesNotExist:
            return Http404
    def get(self, request, pk):
        profesor = self.get_object(pk)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profesor = self.get_object(pk)
        profesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#INSTITUCION
def panelInstitucion(request):
    formInstitucion = forms.InstitucionForm()
    instituciones = Institucion.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        institucion = Institucion()
        if( len(nombre) > 0 ):
            institucion.nombre = nombre
            institucion.save()
            return redirect(to=panelInstitucion)
    datos = {'form':formInstitucion,'instituciones':instituciones}
    return render(request,'institucion/panelInstitucion.html',datos)

#DIRECCION
def panelDireccion(request):
    formDireccion = forms.DireccionForm()
    direcciones = Direccion.objects.all()
    if request.method == 'POST':
        formDireccion = forms.DireccionForm(request.POST)
        if formDireccion.is_valid():
            ciudad = formDireccion['ciudad'].value()
            calle = formDireccion['calle'].value()
            numero = formDireccion['numero'].value()
            direccion = Direccion()
            direccion.ciudad = ciudad
            direccion.calle = calle
            direccion.numero = numero
            direccion.save()
            return redirect(to=panelDireccion)
    datos = {'form':formDireccion, 'direcciones':direcciones}
    return render(request,'direccion/panelDireccion.html',datos)


def editarDireccion(request,id):
    direccion = get_object_or_404(Direccion, id=id)
    data = {
        'form': forms.DireccionForm(instance=direccion)
    }
    if request.method == 'POST':
        formulario = forms.DireccionForm(data=request.POST, instance=direccion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=panelDireccion)
        else:
            data["form"] = formulario
    return render(request, 'direccion/panelDireccion.html', data)

def eliminarDireccion(request, id):
    direccion = get_object_or_404(Direccion, id = id)
    direccion.delete()
    return redirect(to='/panelDireccion')
"""