from django import forms
from models import Carrera, Ciclo

"""
Simple Modelform for Institucion
"""
class CarreraForm(forms.ModelForm):
	class Meta:
		model = Carrera

class CicloForm(forms.ModelForm):
	class Meta:
		model = Ciclo
