# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.db.models import Q
from models import Boleta
from alumno.models import Alumno
from campus.models import Campus
import datetime

numero_boleta = "0000000"
serie_boleta = "000"

def get_serie_numero():
    numero_serie = Boleta.objects.values("serie","numero").order_by("-serie","-numero")
    if len(numero_serie)==0:
        numero_serie = {'serie':'001','numero':'0000001',}
    else:
        numero_serie = numero_serie[0]
        if(int(numero_serie["numero"]==9999999)):
            numero_serie["numero"] = "0000001"
            nueva_serie = str(int(numero_serie["serie"])+1)
            numero_serie["serie"] = serie_boleta[3:-len(int(nueva_serie))]+nueva_serie
        else:
            nuevo_numero = str(int(numero_serie["numero"])+1)
            numero_serie["numero"] = numero_boleta[0:7-len(nuevo_numero)]+nuevo_numero
    return numero_serie

def boletas(request):
    date_ini = datetime.datetime.today().replace(minute=0,hour=0)
    boletas = Boleta.objects.filter(fecha_emision__range=(date_ini,datetime.datetime.today())).order_by("-fecha_emision")
    return render(request, "boleta/boletas.html",{ 'boletas':boletas, },)

def alumno_boleta_json(request,codigo_alumno):
    alumno = Alumno.objects.get(codigo = codigo_alumno)
    campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
    boleta_json = {
                      "codigo" : alumno.codigo,
                      "alumno" : u'%s %s' % (alumno.apellido, alumno.nombre),
                      "turno" : campus[0].campus.turno,
                      "ciclo_seccion" : u'%s - %s' % (campus[0].campus.ciclo.ciclo, campus[0].campus.get_seccion()),
                      "carrera" : campus[0].campus.ciclo.carrera.carrera,
                      "precio_pension" : str(campus[0].campus.ciclo.carrera.precio),
                      }
    return HttpResponse(simplejson.dumps(boleta_json),mimetype='application/json')

def alumno_boleta_nombre_json(request):
    alumno = request.GET.get('term')
    alumnos = Alumno.objects.values('codigo', 'nombre', 'apellido').filter(Q(nombre__icontains = alumno) | Q(apellido__icontains = alumno), Q(matriculado = True))
    resultado = [{'id' : alumnoselect['codigo'], 'value' : u'%s, %s' % (alumnoselect['apellido'], alumnoselect['nombre'])} for alumnoselect in alumnos]
    return HttpResponse(simplejson.dumps(resultado),mimetype='application/json')

def boleta_imprimir(request, boleta_id, campus_id):
    boleta = Boleta.objects.get(pk = boleta_id)
    campus = Campus.objects.get(pk = campus_id)
    return render(request, 'boleta/boleta_imprimir.html', {'boleta' : boleta, 'campus' : campus})
