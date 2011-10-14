# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Boleta
import datetime

def pago_pension(request):
    if request.method == 'POST':
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        monto = campus[0].monto
        pensiones = campus[0].monto.pension_set.filter(saldo__gt=0)[:1]
        pension = pensiones[0]
        pension.total=pension.total+Decimal(request.POST["monto"])
        pension.saldo=pension.saldo-Decimal(request.POST["monto"])
        boleta = Boleta.objects.create(
                                    alumno = alumno,
                                    serie = request.POST["codigo_boleta"][0:3],
                                    numero =request.POST["codigo_boleta"][4:11],
                                    concepto = request.POST["concepto"],
                                    fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                                    valido = True,
                                    monto = Decimal(request.POST["monto"]),
                                    saldo = Decimal(request.POST["saldo"])
                                    )
        monto.deuda = monto.total+Decimal(request.POST["monto"])
        monto.deuda = monto.deuda-Decimal(request.POST["monto"])
        monto.save()
        pension.save()
        boleta.save()
        Pago.objects.create(boleta=boleta,pension=pension).save()
        return HttpResponseRedirect('/wvb/pension')
    numero_serie=Boleta.objects.values("serie","numero").order_by("-serie","-numero")
    if len(numero_serie)==0:
        numero_serie={'serie':'001','numero':'0000001',}
    else:
        numero_serie=numero_serie[0]
        if(int(numero_serie["numero"]==9999999)):
            numero_serie["numero"]="0000001"
            nueva_serie = str(int(numero_serie["serie"])+1)
            numero_serie["serie"]=serie_boleta[3:-len(int(nueva_serie))]+nueva_serie
        else:
            nuevo_numero = str(int(numero_serie["numero"])+1)
            numero_serie["numero"]=numero_boleta[0:7-len(nuevo_numero)]+nuevo_numero
    return render(request, 'boleta/pago_pension.html', { 'numero_serie': numero_serie, },)

def pago_nota(request):
    docentes = Docente.objects.filter(activo=True)
    if request.method == 'POST':
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        campus = alumno.alumnoscampus_set.all().order_by("-id")[:1]
        monto = campus[0].monto
        pensiones = campus[0].monto.pension_set.filter(saldo__gt=0)[:1]
        pension = pensiones[0]
        pension.total=pension.total+Decimal(request.POST["monto"])
        pension.saldo=pension.saldo-Decimal(request.POST["monto"])
        boleta = Boleta.objects.create(
                                    alumno = alumno,
                                    serie = request.POST["codigo_boleta"][0:3],
                                    numero =request.POST["codigo_boleta"][4:11],
                                    concepto = request.POST["concepto"],
                                    fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
                                    valido = True,
                                    monto = Decimal(request.POST["monto"]),
                                    saldo = Decimal(request.POST["saldo"])
                                    )
        monto.deuda = monto.total+Decimal(request.POST["monto"])
        monto.deuda = monto.deuda-Decimal(request.POST["monto"])
        monto.save()
        pension.save()
        boleta.save()
        Pago.objects.create(boleta=boleta,pension=pension).save()
        Recuperacion.objects.create(nota = Nota.objects.get(pk=request.POST["curso"]), boleta = boleta).save()
        return HttpResponseRedirect('/wvb/recuepracion')
    numero_serie=Boleta.objects.values("serie","numero").order_by("-serie","-numero")
    if len(numero_serie)==0:
        numero_serie={'serie':'001','numero':'0000001',}
    else:
        numero_serie=numero_serie[0]
        if(int(numero_serie["numero"]==9999999)):
            numero_serie["numero"]="0000001"
            nueva_serie = str(int(numero_serie["serie"])+1)
            numero_serie["serie"]=serie_boleta[3:-len(int(nueva_serie))]+nueva_serie
        else:
            nuevo_numero = str(int(numero_serie["numero"])+1)
            numero_serie["numero"]=numero_boleta[0:7-len(nuevo_numero)]+nuevo_numero
    return render(request, 'boleta/pago_nota.html', { 'numero_serie': numero_serie, 'docentes':docentes,},)

def pago(request):
    if request.method == 'POST':
        alumno = Alumno.objects.get(codigo=request.POST["codigo_alumno"])
        boleta = Boleta.objects.create(
            alumno = alumno,serie = request.POST["codigo_boleta"][0:3],
            numero =request.POST["codigo_boleta"][4:11],
            concepto = request.POST["concepto"],
            fecha_emision = datetime.datetime.strptime(request.POST["fecha_emision"],'%d/%m/%Y %H:%M:%S'),
            valido = True,
            monto = Decimal(request.POST["monto"]),
            saldo = 0
            )
        boleta.save()
        return HttpResponseRedirect('/wvb/pago')
    numero_serie=Boleta.objects.values("serie","numero").order_by("-serie","-numero")
    if len(numero_serie)==0:
        numero_serie={'serie':'001','numero':'0000001',}
    else:
        numero_serie=numero_serie[0]
        if(int(numero_serie["numero"]==9999999)):
            numero_serie["numero"]="0000001"
            nueva_serie = str(int(numero_serie["serie"])+1)
            numero_serie["serie"]=serie_boleta[3:-len(int(nueva_serie))]+nueva_serie
        else:
            nuevo_numero = str(int(numero_serie["numero"])+1)
            numero_serie["numero"]=numero_boleta[0:7-len(nuevo_numero)]+nuevo_numero
    return render(request, 'boleta/pago_general.html', { 'numero_serie': numero_serie, },)

def boletas(request):
    date_ini = datetime.datetime.today().replace(minute=0,hour=0)
    boletas = Boleta.objects.filter(fecha_emision__range=(date_ini,datetime.datetime.today())).order_by("-fecha_emision")
    return render(request, "boleta/boletas.html",{ 'boletas':boletas, },)

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
                pension.total=pension.total-boleta.monto
                pension.saldo=pension.saldo+boleta.monto
                pension.save()
                monto = pension.monto
                monto.deuda=monto.deuda+boleta.monto
                monto.total=monto.total-boleta.monto
                monto.save()
        return HttpResponseRedirect('/wvb/anular')
    return render(request, 'boleta/anular.html',)
