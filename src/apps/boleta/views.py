# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db import connection
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

@login_required(login_url='/wvb/')
def boletas(request):
    date_ini = datetime.datetime.today().replace(minute=0,hour=0)
    boletas = Boleta.objects.filter(fecha_emision__range=(date_ini,datetime.datetime.today())).order_by("-fecha_emision")
    return render(request, "boleta/boletas.html",{ 'boletas':boletas, },)

@login_required(login_url='/wvb/')
def alumno_boleta_json(request,codigo_alumno):
    alumno = Alumno.objects.get(codigo = codigo_alumno)
    campus = alumno.alumnocampus_set.all().order_by("-id")[:1]
    boleta_json = {
                      "codigo" : alumno.codigo,
                      "alumno" : u'%s %s' % (alumno.apellido, alumno.nombre),
                      "turno" : campus[0].campus.get_turno().encode("ascii","ignore"),
                      "ciclo_seccion" : u'%s - %s' % (campus[0].campus.ciclo.ciclo, campus[0].campus.get_seccion()),
                      "carrera" : campus[0].campus.ciclo.carrera.carrera,
                      "precio_pension" : str(campus[0].campus.precio.precio),
                      }
    return HttpResponse(simplejson.dumps(boleta_json),mimetype='application/json')

@login_required(login_url='/wvb/')
def alumno_boleta_nombre_json(request):
    alumno = request.GET.get('term')
    alumnos = Alumno.objects.values('codigo', 'nombre', 'apellido').filter(Q(nombre__icontains = alumno) | Q(apellido__icontains = alumno), Q(matriculado = True))
    resultado = [{'id' : alumnoselect['codigo'], 'value' : u'%s, %s' % (alumnoselect['apellido'], alumnoselect['nombre'])} for alumnoselect in alumnos]
    return HttpResponse(simplejson.dumps(resultado),mimetype='application/json')

@login_required(login_url='/wvb/')
def boleta_imprimir(request, boleta_id, campus_id):
    boleta = Boleta.objects.get(pk = boleta_id)
    campus = Campus.objects.get(pk = campus_id)
    return render(request, 'boleta/boleta_imprimir.html', {'boleta' : boleta, 'campus' : campus})

@login_required(login_url='/wvb/')
def boleta_json(request, serie, numero):
    cursor = connection.cursor()
    boleta = cursor.execute("SELECT * FROM boleta_alumno WHERE serie = '%s' AND numero = '%s'" % (serie, numero)).fetchone()
    boleta_json = {
				  "valido" : boleta[0],
				  "serie" : boleta[1],
				  "saldo" : str(boleta[2]),
				  "numero" : boleta[3],
				  "fecha" : str(boleta[4]),
				  "importe" : str(boleta[5]),
				  "concepto" : boleta[6],
				  "alumno" : u'%s, %s' % (boleta[7],boleta[8]),
				  "codigo" : boleta[9],
				  }
    return HttpResponse(simplejson.dumps(boleta_json), mimetype='application/json')
