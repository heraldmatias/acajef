from django import forms
from models import *

class CarreraForm(forms.ModelForm):
	class Meta:
		model = Carrera

class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus

class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta