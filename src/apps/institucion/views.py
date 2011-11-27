# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models import Carrera, Ciclo
from forms import CarreraForm

CICLOS = ('I','II','III','IV','V','VI','VII','VIII','IX','X',)

@login_required(login_url='/wvb/')
def carrera(request):
    carrera_form = CarreraForm()
    if request.method == 'POST':
        carrera_form = CarreraForm(request.POST)
        if carrera_form.is_valid():
            carrera_form.save()
            ciclos = int(request.POST["N"])
            for i in range(0,ciclos):
                Ciclo.objects.create(carrera = carrera_form.instance, ciclo = CICLOS[i]).save()
            Ciclo.objects.create(carrera = carrera_form.instance,ciclo = 'Egresado').save()
            Ciclo.objects.create(carrera = carrera_form.instance,ciclo = 'Pre-Matriculado').save()
            return redirect('/institucion/carrera')
    carreras = Carrera.objects.all().order_by('carrera')
    return render(request,
                'institucion/carrera.html', 
                {'carrera_form' : carrera_form,'carreras' : carreras,},
                )

@login_required(login_url='/wvb/')
def carrera_json(request,carrera_id):
    json_array = []
    carrera = Carrera.objects.get(pk=carrera_id)
    json_array.append(carrera)
    ciclos =  Ciclo.objects.filter(carrera=carrera)
    for ciclo in ciclos:
        json_array.append(ciclo)
    json_serializer = serializers.get_serializer("json")()
    resultado = json_serializer.serialize(json_array, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')

@login_required(login_url='/wvb/')
def cilos_json(request,carrera_id):
    json_array = []
    carrera = Carrera.objects.get(pk=carrera_id)
    ciclos =  Ciclo.objects.filter(carrera=carrera).order_by('pk')
    for ciclo in ciclos:
        json_array.append(ciclo)
    json_serializer = serializers.get_serializer("json")()
    resultado = json_serializer.serialize(json_array, ensure_ascii=False)
    return HttpResponse(resultado,mimetype='application/json')
