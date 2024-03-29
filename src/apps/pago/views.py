# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from boleta.models import Boleta
from concepto.models import Concepto
from boleta.views import get_serie_numero
from alumno.models import Alumno
from docente.models import Docente
from calificacion.models import Recuperacion, Nota
from django.db.models import Q
from boleta.forms import BoletaForm
from campus.models import AlumnoCampus
import datetime

@login_required(login_url='/wvb/')
def pago_pension(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        importe = Decimal(request.POST["importe"])
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        alumnocampus = AlumnoCampus.objects.get(Q(actual = True), Q(alumno = alumno))
        boleta = Boleta.objects.create(
                        alumno = alumnocampus,
                        serie = numero_serie["serie"],
                        numero = numero_serie["numero"],
                        concepto = alumnocampus.campus.precio,
                        fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                        valido = True,
                        importe = importe,
                        saldo = Decimal(request.POST["saldo"])
                    )
        boleta.save()
        alumnocampus.deuda = alumnocampus.deuda - importe
        alumnocampus.total = alumnocampus.total + importe
        alumnocampus.save()
        return redirect(u'%s/' % (boleta.get_url_imprimir()))
    numero_serie = get_serie_numero()
    return render(request, 'pago/pago_pension.html', { 'numero_serie': numero_serie, },)

@login_required(login_url='/wvb/')
def pago_subsanacion(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        importe = Decimal(request.POST["importe"])
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        alumnocampus = AlumnoCampus.objects.get(Q(actual = True), Q(alumno = alumno))
        boleta = Boleta.objects.create(
                        alumno = alumnocampus,
                        serie = numero_serie["serie"],
                        numero = numero_serie["numero"],
                        concepto = Concepto.objects.get(pk = request.POST['concepto']),
                        fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                        valido = True,
                        importe = importe,
                        saldo = Decimal(request.POST["saldo"])
                    )
        boleta.save()
        Recuperacion.objects.create(nota = Nota.objects.get(pk = request.POST["curso"]), boleta = boleta).save()
        return redirect(u'%s/' % (boleta.get_url_imprimir()))
    numero_serie = get_serie_numero()
    docentes = Docente.objects.filter(activo=True)
    conceptos = Concepto.objects.filter(concepto__icontains = 'Subsanar')
    return render(request, 'pago/pago_nota.html', { 'numero_serie': numero_serie, 'docentes':docentes,'conceptos':conceptos},)

@login_required(login_url='/wvb/')
def pago_general(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        alumno = Alumno.objects.get(codigo = request.POST["codigo_alumno"])
        alumnocampus = AlumnoCampus.objects.get(Q(actual = True), Q(alumno = alumno))
        boleta = Boleta.objects.create(
                alumno = alumnocampus,
                serie = numero_serie["serie"],
                numero = numero_serie["numero"],
                concepto = Concepto.objects.get(pk = request.POST["concepto"]),
                fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                valido = True,
                importe = Decimal(request.POST["importe"]),
                saldo = 0
            )
        boleta.save()
        return redirect(u'%s/' % (boleta.get_url_imprimir()))
    numero_serie = get_serie_numero()
    conceptos = Concepto.objects.exclude(concepto__icontains='Pensi')
    boleta_form = BoletaForm()
    return render(request, 'pago/pago_general.html', { 'numero_serie': numero_serie, 'boleta_form' : boleta_form, "conceptos" : conceptos},)

@login_required(login_url='/wvb/')
def anular(request):
    if request.method == 'POST':
        boleta = Boleta.objects.get(
            serie = request.POST["serie"],
            numero = request.POST["numero"],
        )
        boleta.valido = False
        boleta.save()
        return redirect('/pago/anular')
    return render(request, 'pago/anular.html',)
