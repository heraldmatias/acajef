# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import DocenteForm

def docente(request):
    docente_form = DocenteForm()
    docentes_activos = Docente.objects.filter(activo=True).order_by('dni')
    docentes_inactivos = Docente.objects.filter(activo=False).order_by('dni')
    return render(request, 'docente/docente.html', { 'docente_form': docente_form ,"docentes_activos":docentes_activos,"docentes_inactivos":docentes_inactivos},)
