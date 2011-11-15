# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from institucion.forms import CicloForm
from institucion.models import Carrera, Ciclo
from pago.models import Pension
from docente.models import Docente
from curso.models import Curso, CursoDocente
from alumno.models import Alumno
from models import Campus, AlumnoCampus
from calificacion.models import Nota
from boleta.forms import ConceptoForm
from forms import CampusForm, CampusSearchForm
from datetime import timedelta, date, datetime
from django.db.models import Q

from xhtml2pdf import pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

code = "000000"

@login_required(login_url='/wvb/')
def campus(request):
    if request.method == 'POST':
        fecha_inicio = datetime.strptime(str(request.POST["fecha_inicio"]),'%d/%m/%Y'),
        fecha_fin = datetime.strptime(str(request.POST["fecha_fin"]),'%d/%m/%Y'),
        ciclo = Ciclo.objects.get(pk = request.POST["ciclo"])
        concepto = ConceptoForm(request.POST)
        if concepto.is_valid():
            concepto.save()
        campus = Campus.objects.create(
                     ciclo = ciclo,
                     seccion = request.POST["seccion"],
                     semestre = 0 if (fecha_inicio[0].month <=6) else 1,
                     fecha_inicio = fecha_inicio[0],
                     fecha_fin = fecha_fin[0],
                     turno = request.POST["turno"],
                     precio = concepto.instance)
        campus.save()
        cursos = request.POST.getlist("cursos")
        matriculas = request.POST.getlist("matricular")
        decentes = request.POST.getlist("docente")
        for index in range(0, len(cursos)):
            curso_docente = CursoDocente.objects.create(
                                curso = Curso.objects.get(pk=cursos[index]),
                                docente = Docente.objects.get(pk=decentes[index]),
                                campus = campus)
            curso_docente.save()
        for matricula in matriculas:
            alumno = Alumno.objects.get(pk=matricula)
            if not alumno.matriculado:
                alumno.matriculado = True
                total_alumnos = (Alumno.objects.exclude(codigo="").count()+1)
                alumno.codigo = code[0:(len(code)-len(str(total_alumnos)))]+str(total_alumnos)
                alumno.save()
            AlumnoCampus(alumno = alumno,campus = campus,total = 0, deuda = campus.precio.precio*ciclo.carrera.duracion).save()
        return redirect('/campus/nuevo/listar/'+str(campus.pk)+'/')
    campus_form = CampusForm()
    campus_search_form = CampusSearchForm()
    ciclo_form = CicloForm()
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('pk')
    conceptoform = ConceptoForm()
    docentes = Docente.objects.filter(activo=True)
    alumnos_no_matriculados = Alumno.objects.filter(matriculado=False)
    return render(request,
                    'campus/campus.html',
                    { 'campus_form': campus_form, "campus_search_form" : campus_search_form, "ciclo_form":ciclo_form,"carrera":carrera,"docentes":docentes,"alumnos_no_matriculados":alumnos_no_matriculados,'ciclos':ciclos, 'conceptoform' : conceptoform})

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
    campusalumno = AlumnoCampus.objects.filter(campus = campus)
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('-pk')
    return render(request,
                    'campus/campus-listar.html',
                    {'campus_search_form' : campus_search_form, "ciclos" : ciclos, 'campusalumno' : campusalumno, })

@login_required(login_url='/wvb/')
def campus_lista_asistencia(request, campus_id):
    nombre_dia = ['Lun','Mar','Mie','Jue','Vie']
    campus = Campus.objects.get(pk = campus_id)
    alumnos = AlumnoCampus.objects.filter(campus = campus)
    fecha_inicio = campus.fecha_inicio
    fecha_fin = campus.fecha_fin
    semanas = fecha_fin - fecha_inicio 
    dias = []
    asistencia = []
    for d in range(0,(semanas.days+1)):
        fecha = fecha_inicio + timedelta(days = d)
        if not (fecha.weekday()==5 or  fecha.weekday()==6):
            dias.append((nombre_dia[fecha.weekday()],fecha.day))
        if len(dias) == 10:
            asistencia.append(dias)
            dias = []
    if len(dias) > 0:
        asistencia.append(dias)
    pdf_html_lista = render_to_string('campus/campus-lista-asistencia.html',
                         { 'campus' : campus, "alumnos" : alumnos, 'asistencia' : asistencia,},
                         context_instance=RequestContext(request))
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(pdf_html_lista.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(pdf_html_lista))

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

@login_required(login_url='/wvb/')
def registro_academico(request):
    if request.method == 'POST':
        alumnos = request.POST.getlist("alumnos")
        notas = request.POST.getlist("notas")
        campus = Campus.objects.get(pk = request.POST["campus"])
        cursodocente = CursoDocente.objects.get(pk = request.POST["cursos_docente"])
        for index,alumno in enumerate(alumnos):
            Nota.objects.create(
                alumno_campus = AlumnoCampus.objects.get(Q(alumno = Alumno.objects.get(pk = alumno)) , Q(campus = campus)),
                curso_docente = cursodocente,
                nota = notas[index]).save()
        return redirect('/campus/registro-academico/')
    carrera = Carrera.objects.get(pk=1)
    campus_search_form = CampusSearchForm()
    carrera = Carrera.objects.get(pk=1)
    ciclos = carrera.ciclo_set.all().order_by('pk')
    return render(request, 'campus/registro_academico.html', { 'campus_search_form': campus_search_form,'ciclos':ciclos },)

@login_required(login_url='/wvb/')
def registro_academico_ajax(request,ciclo_id,ano,seccion,turno,semestre):
    try:
        campus = Campus.objects.get(
                    fecha_inicio__year = ano,
                    seccion = seccion,
                    semestre = semestre,
                    turno = turno,
                    ciclo = Ciclo.objects.get(pk=ciclo_id))
        alumnos = campus.alumnocampus_set.all()
        docentes = CursoDocente.objects.filter(~Q(pk__in = Nota.objects.values('curso_docente').filter(alumno_campus__in = alumnos).distinct()), Q(campus = campus))
    except:
        return render(request, 'campus/registro_academico_ajax.html')
    return render(request, 'campus/registro_academico_ajax.html', { 'alumnos': alumnos,'docentes':docentes,"campus":campus,})
