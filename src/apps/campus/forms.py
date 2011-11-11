# -*- coding: utf-8 -*-
from django import forms
from models import Campus, TURNO, SEMESTRE
from institucion.models import Carrera
import datetime

"""
Simple ModelForm for Campus
"""

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus

class CampusSearchForm(forms.Form):
	search_years    = forms.IntegerField(widget=forms.Select(choices=[(year, year) for year in range(1965, datetime.date.today().year+1)]))
	search_carrera  = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all())
	search_semestre = forms.IntegerField(widget=forms.Select(choices=SEMESTRE))
	search_turno    = forms.IntegerField(widget=forms.Select(choices=TURNO))
