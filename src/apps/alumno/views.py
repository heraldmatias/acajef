# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from institucion.models import Carrera, Ciclo
from concepto.models import Concepto
from boleta.views import get_serie_numero
from boleta.models import Boleta
from campus.models import AlumnoCampus, Campus
from forms import AlumnoForm
import datetime

@login_required(login_url='/wvb/')
def alumno(request):
    serie_numero = get_serie_numero()
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, request.FILES)
        print alumno_form.is_valid()
        if alumno_form.is_valid():
            alumno_form.save()
            ciclo = Ciclo.objects.get(Q(carrera = Carrera.objects.get(pk = request.POST['carrera'])), Q(ciclo__icontains = 'Pre-M'))
            concepto = Concepto.objects.get(pk = request.POST['concepto'])
            campus = Campus.objects.create(
                        ciclo =  ciclo,
                        semestre = 0,
                        turno = 0,
                        seccion = 0,
                        fecha_inicio = datetime.datetime.today(),
                        fecha_fin = datetime.datetime.today(),
                        precio = concepto
                        )
            campus.save()
            alumno_campus = AlumnoCampus.objects.create(
                    alumno = alumno_form.instance,
                    campus = campus,
                    total = 0,
                    deuda = 0,
                    confirmado = True,
                    actual =True
                    )
            alumno_campus.save()
            boleta = Boleta.objects.create(
                        alumno = alumno_campus,
                        serie = serie_numero["serie"],
                        numero = serie_numero["numero"],
                        concepto = concepto,
                        fecha_emision = datetime.datetime.today(),
                        valido = True,
                        importe = concepto.precio,
                        saldo = 0
                        )
            boleta.save()
            return redirect(u'%s/' % (boleta.get_url_imprimir()))
    alumno_form = AlumnoForm()
    carreras = Carrera.objects.all()
    conceptos = Concepto.objects.filter(concepto__icontains = 'Pre')
    return render(request,
                    'alumno/alumno.html', 
                    { 'alumno_form' : alumno_form, 'carreras' : carreras, 'conceptos' : conceptos, 'serie_numero':serie_numero})
