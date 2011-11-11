# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from institucion.forms import CicloForm
from institucion.models import Carrera, Ciclo
from pago.models import Monto, Pension, Pago
from docente.models import Docente
from curso.models import Curso, CursoDocente
from alumno.models import Alumno
from models import Campus, AlumnosCampus
from forms import CampusForm, CampusSearchForm
import datetime

code = "000000"

@login_required(login_url='/wvb/')
def campus(request):
    if request.method == 'POST':
        arr_obj=[]
        fecha_inicio = datetime.datetime.strptime(str(request.POST["fecha_inicio"]),'%d/%m/%Y'),
        fecha_fin = datetime.datetime.strptime(str(request.POST["fecha_fin"]),'%d/%m/%Y'),
        ciclo = Ciclo.objects.get(pk = request.POST["ciclo"])
        campus = Campus.objects.create(
                     ciclo = ciclo,
                     seccion = request.POST["seccion"],
                     semestre = 1 if (fecha_inicio[0].month <=6) else 2,
                     fecha_inicio = fecha_inicio[0],
                     fecha_fin = fecha_fin[0],
                     turno = request.POST["turno"])
        arr_obj.append(campus)
        cursos = request.POST.getlist("cursos")
        matriculas = request.POST.getlist("matricular")
        decentes = request.POST.getlist("docente")
        for index in range(0, len(cursos)):
            curso_docente = CursoDocente.objects.create(
                                curso = Curso.objects.get(pk=cursos[index]),
                                docente = Docente.objects.get(pk=decentes[index]),
                                campus = campus)
            arr_obj.append(curso_docente)
        for matricula in matriculas:
            monto_alumno = Monto.objects.create(
                               deuda = ciclo.carrera.precio*ciclo.carrera.duracion,
                               total = 0,
                               n_pension = 0,
                               n_pago = 0,)
            arr_obj.append(monto_alumno)
            for i in range(0, ciclo.carrera.duracion):
				pension = Pension.objects.create(
							  monto = monto_alumno,
							  total = 0,
							  fecha_vencimiento = datetime.date.today(),
							  saldo = ciclo.carrera.precio)
				arr_obj.append(pension)
            alumno = Alumno.objects.get(pk=matricula)
            if not alumno.matriculado:
                alumno.matriculado = True
                total_alumnos = (Alumno.objects.exclude(codigo="").count()+1)
                alumno.codigo = code[0:(len(code)-len(str(total_alumnos)))]+str(total_alumnos)
                alumno.save()
            alumno_campus = AlumnosCampus(alumno = alumno,campus = campus,monto=monto_alumno)
            arr_obj.append(alumno_campus)
        for objeto in arr_obj:
            objeto.save()
        return redirect('/campus/nuevo/listar/'+str(campus.pk)+'/')
    campus_form = CampusForm()
    campus_search_form = CampusSearchForm()
    ciclo_form = CicloForm()
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('-pk')
    docentes = Docente.objects.filter(activo=True)
    alumnos_no_matriculados = Alumno.objects.filter(matriculado=False)
    return render(request,
                    'campus/campus.html',
                    { 'campus_form': campus_form, "campus_search_form" : campus_search_form, "ciclo_form":ciclo_form,"carrera":carrera,"docentes":docentes,"alumnos_no_matriculados":alumnos_no_matriculados,'ciclos':ciclos })

@login_required(login_url='/wvb/')
def campus_listar(request):
    campus_search_form = CampusSearchForm()
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('-pk')
    return render(request,
                    'campus/campus-listar.html',
                    { 'campus_search_form': campus_search_form,"ciclos":ciclos, })

@login_required(login_url='/wvb/')
def campus_new_listar(request, campus_id):
    campus_search_form = CampusSearchForm()
    campus = Campus.objects.get(pk = campus_id)
    campusalumno = AlumnosCampus.objects.filter(campus = campus)
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('-pk')
    return render(request,
                    'campus/campus-listar.html',
                    {'campus_search_form' : campus_search_form, "ciclos" : ciclos, 'campusalumno' : campusalumno, })

@login_required(login_url='/wvb/')
def campus_matriculado(request, carrera_id, ano, turno):
    ciclos = Carrera.objects.get(pk=carrera_id).ciclo_set.all()
    campus_get = Campus.objects.filter(ciclo__in = ciclos, fecha_inicio__year = ano,turno = turno)
    json_array = [{ "ciclo" : campus.ciclo.ciclo , "seccion" : campus.seccion, "id" : campus.pk  } for campus in campus_get]
    return HttpResponse(simplejson.dumps(json_array),mimetype='application/json')

@login_required(login_url='/wvb/')
def campus_matriculado_alumno(request, campus_id):
    campus = Campus.objects.get(pk = campus_id)
    campus_alumno_get = AlumnosCampus.objects.filter(campus = campus)
    json_array = [{ "id" : campus.alumno.pk , "dni" : campus.alumno.dni, "nombre" : campus.alumno.nombre, "apellido" : campus.alumno.apellido } for campus in campus_alumno_get]
    return HttpResponse(simplejson.dumps(json_array),mimetype='application/json')
