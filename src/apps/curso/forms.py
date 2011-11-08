from django import forms
from models import Curso

"""
Simple Modelform for Curso
"""
class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
