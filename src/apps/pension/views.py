# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from decimal import Decimal
from models import Pension
from boleta.models import Boleta
from boleta.views import get_serie_numero
from alumno.models import Alumno
from docente.models import Docente
from boleta.forms import BoletaForm
import datetime

def pago_pension(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        importe = Decimal(request.POST["importe"])
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        boleta = Boleta.objects.create(
                        alumno = alumno,
                        serie = numero_serie["serie"],
                        numero =numero_serie["numero"],
                        concepto = request.POST["concepto"],
                        fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                        valido = True,
                        importe = importe,
                        saldo = Decimal(request.POST["saldo"])
					)
        boleta.save()
        Pension.objects.create(alumno_campus = campus, boleta = boleta).save()
        return redirect(u'%s/%s' % (boleta.get_url_imprimir(),str(campus[0].campus.id)))
    numero_serie = get_serie_numero()
    return render(request, 'pago/pago_pension.html', { 'numero_serie': numero_serie, },)

def pago_subsanacion(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        importe = Decimal(request.POST["importe"])
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        boleta = Boleta.objects.create(
                        alumno = alumno,
                        serie = numero_serie["serie"],
                        numero = numero_serie["numero"],
                        concepto = request.POST["concepto"],
                        fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                        valido = True,
                        importe = importe,
                        saldo = Decimal(request.POST["saldo"])
                    )
        boleta.save()
        Recuperacion.objects.create(nota = Nota.objects.get(pk=request.POST["curso"]), boleta = boleta).save()
        return redirect('/pago/subsanacion')
    numero_serie = get_serie_numero()
    docentes = Docente.objects.filter(activo=True)
    return render(request, 'pago/pago_nota.html', { 'numero_serie': numero_serie, 'docentes':docentes,},)

def pago_general(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        alumno = Alumno.objects.get(codigo = request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        boleta = Boleta.objects.create(
                alumno = alumno,
                serie = numero_serie["serie"],
                numero = numero_serie["numero"],
                concepto = request.POST["concepto"],
                fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                valido = True,
                importe = Decimal(request.POST["importe"]),
                saldo = 0
            )
        boleta.save()
        return redirect(u'%s/%s' % (boleta.get_url_imprimir(),str(campus[0].campus.id)))
    numero_serie = get_serie_numero()
    boleta_form = BoletaForm()
    return render(request, 'pago/pago_general.html', { 'numero_serie': numero_serie, 'boleta_form' : boleta_form},)

def anular(request):
    if request.method == 'POST':
        if tipo_boleta == 0:
            boleta = Boleta.objects.get(
                serie = request.POST["codigo_alumno"][0:3],
                numero =request.POST["codigo_alumno"][4:11],
            )
            boleta.valido = False
            boleta.save()
            tipo_boleta = request.POST["codigo_alumno"]
            if tipo_boleta == 1:
                pension=Pago.objetcs.get(boleta=boleta).pension
                pension.total=pension.total-boleta.precio
                pension.saldo=pension.saldo+boleta.precio
                pension.save()
                precio = pension.precio
                precio.deuda=precio.deuda+boleta.precio
                precio.total=precio.total-boleta.precio
                precio.save()
        return redirect('/pago/anular')
    return render(request, 'pago/anular.html',)
