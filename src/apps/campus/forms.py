# -*- coding: utf-8 -*-
from django import forms
from models import Campus, TURNO, SEMESTRE, SECCION
from institucion.models import Carrera
from operator import itemgetter
import datetime

"""
Simple ModelForm for Campus
"""
def get_years():
    years = [(year, year) for year in range(1965, datetime.date.today().year+1)]
    return sorted(years, key=itemgetter(0), reverse=True)

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus

class CampusSearchForm(forms.Form):
    search_years    = forms.IntegerField(widget=forms.Select(choices=get_years()))
    search_carrera  = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all())
    search_semestre = forms.IntegerField(widget=forms.Select(choices=SEMESTRE))
    search_turno    = forms.IntegerField(widget=forms.Select(choices=TURNO))
    search_seccion  = forms.IntegerField(widget=forms.Select(choices=SECCION))
