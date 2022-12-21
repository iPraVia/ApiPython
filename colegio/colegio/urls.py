"""colegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path("admin/", admin.site.urls),   
    path("",views.index, name='index'),
    #CURSO
    path("panelCurso/",views.panelCurso,name='panelCurso'),    
    path("curso/", views.CursoView.as_view(),name='curso'),
    path("curso/<int:pk>", views.CursoDetail.as_view()),
    #PROFESOR
    path("panelProfesor/",views.panelProfesor,name='panelProfesor'), 
    path('profesor/',views.ProfesorView.as_view(),name='profesor'),
    path('profesor/<int:pk>',views.ProfesorDetail.as_view()),
    #ALUMNO
    path("panelAlumno/",views.panelAlumno,name='panelAlumno'), 
    path('alumno/',views.AlumnoView.as_view(),name='alumno'),
    path('alumno/<int:pk>',views.AlumnoDetail.as_view()),
    #DIRECCION
    path('direccion/',views.DireccionView.as_view()),
    path('direccion/<int:pk>',views.DireccionDetail.as_view()),
    #ASIGNATURA
    path("panelAsignatura/",views.panelAsignatura,name='panelAsignatura'), 
    path('asignatura/',views.AsignaturaView.as_view(),name='asignatura'),
    path('asignatura/<int:pk>',views.AsignaturaDetail.as_view()),
    #INSTITUCION
    path("panelInstitucion/",views.panelInstitucion,name='panelInstitucion'), 
    path('institucion/',views.InstitucionView.as_view(), name='institucion'),
    path('institucion/<int:pk>',views.InstitucionDetail.as_view()),
    #CALIFICACION
    path('calificacion/',views.CalificacionView.as_view()),
    path('panelCalificacion/',views.panelCalificacion,name='panelCalificacion'),
]
