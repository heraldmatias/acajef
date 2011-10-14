from django import forms
from models import Carrera, Ciclo

class CarreraForm(forms.ModelForm):
	class Meta:
		model = Carrera

class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
