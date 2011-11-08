from django import forms
from models import Docente

"""
Simple Modelform for Docente
"""
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
