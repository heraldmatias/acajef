# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from boleta.models import Boleta
from boleta.views import get_serie_numero
import datetime

def pago_pension(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        precio = campus[0].precio
        pensiones = campus[0].precio.pension_set.filter(saldo__gt=0)[:1]
        pension = pensiones[0]
        pension.total=pension.total+Decimal(request.POST["precio"])
        pension.saldo=pension.saldo-Decimal(request.POST["precio"])
        boleta = Boleta.objects.create(
                    alumno = alumno,
                    serie = numero_serie["serie"],
                    numero =numero_serie["numero"],
                    concepto = request.POST["concepto"],
                    fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                    valido = True,
                    precio = Decimal(request.POST["precio"]),
                    saldo = Decimal(request.POST["saldo"])
					)
        precio.deuda = precio.total+Decimal(request.POST["precio"])
        precio.deuda = precio.deuda-Decimal(request.POST["precio"])
        precio.save()
        pension.save()
        boleta.save()
        Pago.objects.create(boleta=boleta,pension=pension).save()
        return redirect('/pago/pension')
    numero_serie = get_serie_numero()
    return render(request, 'pago/pago_pension.html', { 'numero_serie': numero_serie, },)

def pago_subsanacion(request):
    docentes = Docente.objects.filter(activo=True)
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        precio = campus[0].precio
        pensiones = campus[0].precio.pension_set.filter(saldo__gt=0)[:1]
        pension = pensiones[0]
        pension.total = pension.total+Decimal(request.POST["precio"])
        pension.saldo = pension.saldo-Decimal(request.POST["precio"])
        boleta = Boleta.objects.create(
                    alumno = alumno,
                    serie = numero_serie["serie"],
                    numero = numero_serie["numero"],
                    concepto = request.POST["concepto"],
                    fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                    valido = True,
                    precio = Decimal(request.POST["precio"]),
                    saldo = Decimal(request.POST["saldo"])
                    )
        precio.deuda = precio.total+Decimal(request.POST["precio"])
        precio.deuda = precio.deuda-Decimal(request.POST["precio"])
        precio.save()
        pension.save()
        boleta.save()
        Pago.objects.create(boleta=boleta,pension=pension).save()
        Recuperacion.objects.create(nota = Nota.objects.get(pk=request.POST["curso"]), boleta = boleta).save()
        return redirect('/pago/subsanacion')
    numero_serie = get_serie_numero()
    return render(request, 'pago/pago_nota.html', { 'numero_serie': numero_serie, 'docentes':docentes,},)

def pago_general(request):
    if request.method == 'POST':
        numero_serie = get_serie_numero()
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        boleta = Boleta.objects.create(
            alumno = alumno,
            serie = numero_serie["serie"],
            numero = numero_serie["numero"],
            concepto = request.POST["concepto"],
            fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
            valido = True,
            precio = Decimal(request.POST["precio"]),
            saldo = 0
            )
        boleta.save()
        return redirect('/pago/general')
    numero_serie = get_serie_numero()
    return render(request, 'pago/pago_general.html', { 'numero_serie': numero_serie, },)

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
