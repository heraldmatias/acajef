from django import forms
from models import Alumno

"""
Simple ModelForm for Alumno
"""

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
