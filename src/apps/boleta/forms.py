from django import forms
from models import Boleta, Concepto

class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta

class ConceptoForm(forms.ModelForm):
    class Meta:
        model = Concepto
