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
from campus.models import Campus, AlumnoCampus
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
def alumno_boleta_json(request,codigo_alumno):
    alumno = Alumno.objects.get(codigo = codigo_alumno)
    alumnocampus = AlumnoCampus.objects.get(Q(actual = True), Q(alumno = alumno))
    boleta_json = {
                      "codigo" : alumno.codigo,
                      "alumno" : u'%s %s' % (alumno.apellido, alumno.nombre),
                      "turno" : alumnocampus.campus.get_turno().encode("ascii","ignore"),
                      "ciclo_seccion" : u'%s - %s' % (alumnocampus.campus.ciclo.ciclo, alumnocampus.campus.get_seccion()),
                      "carrera" : alumnocampus.campus.ciclo.carrera.carrera,
                      "precio_pension" : str(alumnocampus.campus.precio.precio),
                      }
    return HttpResponse(simplejson.dumps(boleta_json),mimetype='application/json')

@login_required(login_url='/wvb/')
def alumno_boleta_nombre_json(request):
    alumno = request.GET.get('term')
    alumnos = Alumno.objects.values('codigo', 'nombre', 'apellido').filter(Q(nombre__icontains = alumno) | Q(apellido__icontains = alumno), Q(matriculado = True))
    resultado = [{'id' : alumnoselect['codigo'], 'value' : u'%s, %s' % (alumnoselect['apellido'], alumnoselect['nombre'])} for alumnoselect in alumnos]
    return HttpResponse(simplejson.dumps(resultado),mimetype='application/json')

@login_required(login_url='/wvb/')
def alumno_boleta_id_json(request):
    alumno = request.GET.get('term')
    alumnos = Alumno.objects.values('id', 'nombre', 'apellido').filter(Q(nombre__icontains = alumno) | Q(apellido__icontains = alumno), Q(matriculado = True))
    resultado = [{'id' : alumnoselect['id'], 'value' : u'%s, %s' % (alumnoselect['apellido'], alumnoselect['nombre'])} for alumnoselect in alumnos]
    return HttpResponse(simplejson.dumps(resultado),mimetype='application/json')

@login_required(login_url='/wvb/')
def boleta_imprimir(request, boleta_id):
    boleta = Boleta.objects.get(pk = boleta_id)
    return render(request, 'boleta/boleta_imprimir.html', {'boleta' : boleta,})

@login_required(login_url='/wvb/')
def boleta_historial(request):
    date_ini = datetime.datetime.today().replace(minute=0,hour=0)
    boletas = Boleta.objects.filter(fecha_emision__range=(date_ini,datetime.datetime.today())).order_by("-fecha_emision")
    return render(request, "boleta/boleta_historial.html",{ 'boletas':boletas, },)

@login_required(login_url='/wvb/')
def boleta_json(request, serie, numero):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.boleta_alumno WHERE serie = '%s' AND numero = '%s'" % (serie, numero))
    boleta = cursor.fetchone()
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

@login_required(login_url='/wvb/')
def boleta_buscar(request, serie, numero, alumno, fecha_inicio, fecha_fin, anulado):
    return HttpResponse(simplejson.dumps(boleta_json), mimetype='application/json')

@login_required(login_url='/wvb/')
def search_boleta_json(request, serie, numero):
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
