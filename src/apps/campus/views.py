# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from institucion.forms import CicloForm
from institucion.models import Carrera
from docente.models import Docente
from alumno.models import Alumno
from models import Campus
from forms import CampusForm

@login_required(login_url='/wvb/')
def campus(request):
    campus_form = CampusForm()
    ciclo_form = CicloForm()
    carrera = Carrera.objects.get(pk=1)
    docentes = Docente.objects.filter(activo=True)
    alumnos_no_matriculados = Alumno.objects.filter(matriculado=False)
    if request.method == 'POST':
        arr_obj=[]
        ciclo=Ciclo.objects.get(pk=request.POST["ciclo"])
        campus = Campus.objects.create(ciclo=ciclo,seccion=request.POST["seccion"],ano=datetime.date.today().year,semestre=request.POST["semestre"],fecha_inicio = datetime.datetime.strptime(str(request.POST["fecha_inicio"]),'%m/%d/%Y') ,fecha_fin = datetime.datetime.strptime(str(request.POST["fecha_fin"]),'%m/%d/%Y'),turno=request.POST["turno"])
        arr_obj.append(campus)
        cursos = request.POST.getlist("cursos")
        matriculas = request.POST.getlist("matricular")
        decentes = request.POST.getlist("docente")
        for index,asignatura in enumerate(cursos):
            curso_docente = CursoDocente.objects.create(curso=Curso.objects.get(pk=asignatura),docente=Docente.objects.get(pk=decentes[index]),campus=campus)
            arr_obj.append(curso_docente)
        for matricula in matriculas:
            monto_alumno = Monto.objects.create(cantidad=ciclo.carrera.duracion,deuda = ciclo.carrera.monto*ciclo.carrera.duracion,total=0)
            arr_obj.append(monto_alumno)
            mt = 1
            while mt <= monto_alumno.cantidad:
                pension = Pension.objects.create(monto=monto_alumno,total = 0,fecha_vencimiento = datetime.date.today(),saldo = carrera.monto)
                arr_obj.append(pension)
                mt+=1
            alumno = Alumno.objects.get(pk=matricula)
            if not alumno.matriculado:
                alumno.matriculado=True
                total_alumnos=(Alumno.objects.exclude(codigo="").count()+1)
                alumno.codigo = code[0:(len(code)-len(str(total_alumnos)))]+str(total_alumnos)
                alumno.save()
            alumno_campus = AlumnosCampus(alumno = alumno,campus = campus,monto=monto_alumno)
            arr_obj.append(alumno_campus)
        for objeto in arr_obj:
            objeto.save()
        return redirect('/wvb/campus')
    return render(request,
                    'campus/campus.html',
                    { 'campus_form': campus_form,"ciclo_form":ciclo_form,"carrera":carrera,"docentes":docentes,"alumnos_no_matriculados":alumnos_no_matriculados })
