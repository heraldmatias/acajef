# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from forms import DocenteForm
from models import Docente

@login_required(login_url='/wvb/')
def docente(request):
    docente_form = DocenteForm()
    if request.method == 'POST':
        docente_form = DocenteForm(request.POST,request.FILES)
        if docente_form.is_valid():
            docente_form.save()
            return redirect('/docente/listar/')
    docentes_activos = Docente.objects.filter(activo=True).order_by('dni')
    docentes_inactivos = Docente.objects.filter(activo=False).order_by('dni')
    return render(request,
        'docente/docente.html',
        {'docente_form': docente_form, "docentes_activos":docentes_activos, "docentes_inactivos":docentes_inactivos},)

@login_required(login_url='/wvb/')
def docente_json(request,docente_id):
    json_d = Docente.objects.filter(pk=docente_id)
    json_serializer = serializers.get_serializer("json")()
    resultado = json_serializer.serialize(json_d, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')
